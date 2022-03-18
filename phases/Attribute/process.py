
from debug import *;

from .self import AttributePhase;

def AttributePhase_process(self, all_blocks, **_):
	enter(f"AttributePhase.process(self.block.rank = {self.block.rank})");
	
	todo = [];
	
	block = self.block;
	hue = (block.rank - 1) / len(all_blocks);
	
	block.attributes["label"] = f"rank = {block.rank}";
	block.attributes["style"] = "filled";
	block.attributes["fillcolor"] = f"{hue} 1 1";
	
	for child in block.children:
		if "attributes" not in child.has_done:
			todo.append(AttributePhase(child));
			child.has_done.add("attributes");
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;


