from node.function_node import FunctionNode
from tag.tag import Tag
from typing import Dict

class FunctionForest:
    def __init__(self) -> None:
        self.nodes: Dict[str, FunctionNode] = {}

    def get_or_create(self, func_id: str) -> FunctionNode:
        if func_id not in self.nodes:
            self.nodes[func_id] = FunctionNode(id=func_id)
        return self.nodes[func_id]
    
    def add_call(self, caller: str, callee: str, confidence: float) -> None:
        caller_node = self.get_or_create(caller)
        callee_node = self.get_or_create(callee)
        caller_node.add_child(callee_node, confidence)
    
    def add_tag(self, func_id: str, tag: Tag) -> None:
        node = self.get_or_create(func_id)
        node.add_tag(tag)