# TODO: Turn into actual model
from classes.forests.tag_forest import TagForest
from classes.ts_tag.tag import Tag

def build_model_forest() -> TagForest:
    forest = TagForest()
    forest.add_tag(Tag("hate_speech", "moderation", "harassment"))
    forest.add_tag(Tag("fake_account", "moderation", "misinformation"))
    forest.add_tag(Tag("mature_warning", "moderation", "abuse"))
    forest.add_tag(Tag("spam", "moderation", "harassment"))
    forest.add_tag(Tag("appeal", "moderation", "transparency"))
    forest.add_tag(Tag("bot_disclosure", "moderation"))
    forest.add_tag(Tag("account_verification", "moderation", "misinformation"))
    forest.add_tag(Tag("fake_news", "moderation", "misinformation"))
    forest.add_tag(Tag("AI_detection", "genAI", "transparency"))
    forest.add_tag(Tag("report", "reporting", "abuse"))
    forest.add_tag(Tag("report_review", "reporting", "transparency"))
    forest.add_tag(Tag("content_removal", "reporting", "abuse"))
    forest.add_tag(Tag("appeal_process", "reporting", "transparency"))
    forest.add_tag(Tag("data_retention", "privacy", "transparency"))
    forest.add_tag(Tag("encryption", "privacy", "security"))
    forest.add_tag(Tag("privacy_policy", "privacy", "transparency"))
    forest.add_tag(Tag("block", "privacy", "abuse"))
    forest.add_tag(Tag("two_factor_auth", "security"))
    return forest