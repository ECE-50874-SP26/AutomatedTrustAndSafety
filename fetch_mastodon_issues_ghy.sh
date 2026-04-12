#!/bin/bash
# Fetch all open issues from mastodon/mastodon using the GitHub CLI
# Usage: bash fetch_masatodon_issues_gh.sh
# Requires: gh (GitHub CLI), authenticated via `gh auth login`

REPO="mastodon/mastodon"
OUTPUT_FILE="mastodon_open_issues.csv"
PER_PAGE=100

echo "Fetching open issues from $REPO..."

# Write CSV header
echo '"number","title","state","author","url","created_at","updated_at","closed_at","labels","assignees","milestone","comments","body"' > "$OUTPUT_FILE"

page=1
total=0

while true; do
    echo "  Fetching page $page..."

    # Fetch a page of issues as JSON
    response=$(gh api \
        "repos/$REPO/issues?state=open&per_page=$PER_PAGE&page=$page" \
        --jq '.[] | select(.pull_request == null) | [
            (.number | tostring),
            .title,
            .state,
            .user.login,
            .html_url,
            .created_at,
            .updated_at,
            (.closed_at // ""),
            ([.labels[].name] | join(", ")),
            ([.assignees[].login] | join(", ")),
            (.milestone.title // ""),
            (.comments | tostring),
            (.body // "")
        ] | @csv')

    # Break if no results returned
    if [ -z "$response" ]; then
        break
    fi

    echo "$response" >> "$OUTPUT_FILE"
    count=$(echo "$response" | wc -l)
    total=$((total + count))
    page=$((page + 1))

    # If fewer than PER_PAGE results, we're on the last page
    if [ "$count" -lt "$PER_PAGE" ]; then
        break
    fi
done

echo ""
echo "Done! Saved $total issues to: $OUTPUT_FILE"
