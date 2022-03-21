
from debug import *;

from phases.InstructionCruciality.self import InstructionCruciality;

from .self import BlockCruciality;

def BlockCruciality_process(self, all_blocks, **_):
	enter(f"BlockCruciality.process(self.block.po = {self.block.po})");
	
	block = self.block;
	
	todo = [];
	
	if not block.is_critical:
		if block.jump is not None:
			dprint(f"appending block {block.rpo}'s jump:");
			todo.append(InstructionCruciality(block.jump, block));
		block.is_critical = True;
		
		for parent in block.parents:
			dprint(f"{block.po} -> {parent.po}");
			if not parent.is_critical:
				todo.append(BlockCruciality(parent));
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;


