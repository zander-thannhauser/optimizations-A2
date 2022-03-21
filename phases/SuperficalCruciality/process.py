
from debug import *;

from phases.InstructionCruciality.self import InstructionCruciality;

from .self import SuperficalCruciality;

def SuperficalCruciality_process(self, **_):
	enter(f"SuperficalCruciality.process(self.block.rpo = {self.block.rpo})");
	
	block = self.block;
	
	todo = [];
	
	for inst in block.instructions:
		match inst.op:
			case "loadI" | "addI" | "add" \
					| "loadAI" | "comp" | "not" | "i2i" \
					| "multI"  | "loadAO" \
					| "cmp_GT" | "cmp_EQ" | "cmp_LT" | "cmp_NE" | "cmp_LE":
				pass;
			case "storeAI" | "iwrite" | "swrite":
				todo.append(InstructionCruciality(inst, block));
			case _:
				dprint(f"inst.op = {inst.op}");
				assert(not "TODO");
	
	for child in block.children:
		if "superfical-cruciality" not in child.has_done:
			todo.append(SuperficalCruciality(child));
			child.has_done.add("superfical-cruciality");
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;






