
from debug import *;

from .self import EmptyBlockRemoval;

def EmptyBlockRemoval_process(self, all_blocks, **_):
	enter(f"EmptyBlockRemoval.process(self.block.rpo = {self.block.rpo})");
	
	todo = [];
	
	block = self.block;
	
	if len(block.instructions) == 0 and block.jump is None:
		
		dprint(f"block.rpo = {block.rpo}");
		
		child, = block.children;
		
		for parent in block.parents:
			dprint(f"block.label = {block.label}");
			if parent.jump is None:
				parent.children[0] = child;
			elif parent.jump.label == block.label:
				if not child.label:
					assert(not "TODO");
				parent.jump.label = child.label;
				parent.children[1] = child;
			else:
				parent.children[parent.children.index(block)] = child;
		
		child.parents += block.parents;
		child.immedate_dominator = block.immedate_dominator;
		
		all_blocks.remove(block);
		
	for child in block.children:
		if "empty-block-removal" not in child.has_done:
			todo.append(EmptyBlockRemoval(child));
			child.has_done.add("empty-block-removal");
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;


