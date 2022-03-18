
from debug import *;

def attribute_phase(block, n, **_):
	
	enter("attribute_phase(block.rank = {block.rank})");
	
	todo = [];
	
	hue = (block.rank - 1) / n;
	
	block.attributes["label"] = f"rank = {block.rank}";
	block.attributes["style"] = "filled";
	block.attributes["fillcolor"] = f"{hue} 1 1";
	
	for child in block.children:
		if "attributes" not in child.has_done:
			todo.append((1, child));
			child.has_done.add("attributes");
	
	exit("return {todo}");
	
	return todo;
