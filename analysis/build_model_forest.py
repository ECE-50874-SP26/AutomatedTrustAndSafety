# TODO: Turn into actual model
from classes.forests.tag_forest import TagForest
from classes.ts_tag.tag import Tag

def build_model_forest() -> TagForest:
    forest = TagForest()
    forest.add_tag(Tag("init", "setup"))
    forest.add_tag(Tag("load", "io"))
    forest.add_tag(Tag("save", "io"))
    forest.add_tag(Tag("compute", "math", "linear"))
    forest.add_tag(Tag("compute", "math", "nonlinear"))
    forest.add_tag(Tag("error", "exception"))
    return forest