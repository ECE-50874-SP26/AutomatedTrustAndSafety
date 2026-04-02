from enum import Enum, auto

class TagNodeValue(Enum):
    Moderation = auto()
    Misinformation = auto()
    Reporting_Flagging = auto()
    Report_Appealing = auto()
    Report_Content_Option = auto()
    User_to_User_Interaction = auto()
    User_to_User_Data_Encryption = auto()
    User_to_User_Data_Management = auto()
    Viewing_Posts_Content = auto()
    Making_Posts_Uploading_Content = auto()
    Account_Creation = auto()
    User_Privacy_Security = auto()
    Personal_Data_Deletion = auto()
    Personal_Data_Mgmt = auto()
    User_Experience = auto()
    Privacy_Policy_Display = auto()
    Content_Recommendation_Logic = auto()
    Content_Blocking_Logic = auto()
    Blocking_User_Options = auto()
    C1 = auto()
    C2 = auto()
    C3 = auto()
    C4 = auto()
    C5 = auto()
    C6 = auto()
    C7 = auto()
    C8 = auto()
    C9 = auto()
    C10 = auto()
    C11 = auto()
    C12 = auto()
    C13 = auto()
    C14 = auto()
    C15 = auto()
    C16 = auto()
    C17 = auto()
    C18 = auto()
    C19 = auto()
    C20 = auto()
    C20A = auto()
    C21 = auto()
    C21A = auto()
    C22 = auto()
    C23 = auto()
    C24 = auto()
    C25 = auto()
    C26 = auto()
    C27 = auto()
    C28 = auto()
    C29 = auto()
    C30 = auto()
    C31 = auto()
    C32 = auto()
    C33 = auto()
    C34 = auto()
    C35 = auto()
    C36 = auto()
    C37 = auto()
    C38 = auto()
    C39 = auto()
    C40 = auto()
    C41 = auto()
    C42 = auto()
    C43 = auto()
    C44 = auto()
    C45 = auto()
    C46 = auto()
    C47 = auto()
    C48 = auto()
    C49 = auto()


class TagNode:
    def __init__(self, value: TagNodeValue):
        self.value = value
        self.parents = set()
        self.children = set()

    def add_child(self, child: "TagNode"):
        """Create a bidirectional parent-child relationship."""
        self.children.add(child)
        child.parents.add(self)

    def remove_child(self, child: "TagNode"):
        """Remove bidirectional relationship."""
        self.children.discard(child)
        child.parents.discard(self)

    def __repr__(self):
        return f"TagNode({self.value.name})"


class Graph:
    def __init__(self):
        self.roots = set()

    def add_root(self, node: TagNode):
        """Add a root node (node with no parents ideally)."""
        self.roots.add(node)

    def remove_root(self, node: TagNode):
        self.roots.discard(node)

    def find_all_nodes(self):
        """Traverse graph and return all reachable nodes."""
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for child in node.children:
                dfs(child)

        for root in self.roots:
            dfs(root)

        return visited

    def __repr__(self):
        return f"Graph(roots={list(self.roots)})"

def main():
    # Create graph
    graph = Graph()

    # Create nodes
    n1 = TagNode(TagNodeValue.C1)
    n2 = TagNode(TagNodeValue.C2)
    n3 = TagNode(TagNodeValue.C3)
    n4 = TagNode(TagNodeValue.C4)
    n5 = TagNode(TagNodeValue.C5)

    # Build relationships
    #      n1
    #     /  \
    #   n2    n3
    #     \  /
    #      n4
    #       |
    #      n5

    n1.add_child(n2)
    n1.add_child(n3)

    n2.add_child(n4)
    n3.add_child(n4)  # n4 has TWO parents

    n4.add_child(n5)

    # Add root(s)
    graph.add_root(n1)

    # Print structure
    print("Roots:", graph.roots)

    all_nodes = graph.find_all_nodes()
    print("All nodes in graph:", all_nodes)

    # Show relationships
    for node in all_nodes:
        print(f"{node}:")
        print(f"  Parents: {[p.value.name for p in node.parents]}")
        print(f"  Children: {[c.value.name for c in node.children]}")


if __name__ == "__main__":
    main()