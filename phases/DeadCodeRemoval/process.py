
from debug import *;

from .self import DeadCodeRemoval;

def DeadCodeRemoval_process(self, **_):
	enter(f"DeadCodeRemoval.process(self.block.rpo = {self.block.rpo})");
	
	block = self.block;
	
	new_instructions = [];
	
	for inst in block.instructions:
		if inst.is_critical:
			new_instructions.append(inst);
		else:
			dprint(f"inst: {inst}");
			del block.valnum_to_instruction[inst.out];
	
	block.instructions = new_instructions;
	
	todo = [];
	for child in block.children:
		if "will-dead-code-remove" not in child.has_done:
			todo.append(DeadCodeRemoval(child));
			child.has_done.add("will-dead-code-remove");
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;


