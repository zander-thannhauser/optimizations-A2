
from debug import *;

from phases.InstructionCruciality.self import InstructionCruciality;

from .self import SuperficalCruciality;

def SuperficalCruciality_process(self, **_):
	enter(f"SuperficalCruciality.process(self.block.rpo = {self.block.rpo})");
	
	block = self.block;
	
	todo = [];
	
	for inst in block.instructions:
		match inst.op:
			case "addI" | "add" | "fadd" | "mult" | "fmult" | "mod" \
					| "load" | "fload" | "loadI" | "loadAI" \
					| "comp" | "not" | "or" | "i2i" | "i2f" | "f2i" \
					| "multI"  | "loadAO" | "sub" | "rshiftI"\
					| "cmp_GT" | "cmp_EQ" | "cmp_LT" | "cmp_NE" | "cmp_LE" \
					| "cmp_GE":
				pass;
			case "call" | "icall"\
				| "store" | "storeAI" | "storeAO" \
				| "iread" | "iwrite" | "swrite" | "putchar":
				todo.append(InstructionCruciality(inst, block));
			case _:
				dprint(f"inst.op = {inst.op}");
				assert(not "TODO");
	
	if block.jump is not None:
		match block.jump.op:
			case "ret" | "iret":
				todo.append(InstructionCruciality(block.jump, block));
			case "cbr" | "cbr_GT" | "cbr_GE" | "cbr_LE" | "cbr_EQ" | "cbr_LT" | "cbrne":
				pass;
			case jop:
				dprint(f"jop = {jop}");
				assert(not "TODO");
	
	for child in block.children:
		if "superfical-cruciality" not in child.has_done:
			todo.append(SuperficalCruciality(child));
			child.has_done.add("superfical-cruciality");
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;






















