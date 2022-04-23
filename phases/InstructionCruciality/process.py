
from debug import *;

from phases.BlockCruciality.self import BlockCruciality;

from ExpressionTable.Phi.self import Phi;

from .self import InstructionCruciality;

def InstructionCruciality_process(self, **_):
	enter(f"InstructionCruciality.process(instruction.out = {self.instruction.out})");
	
	inst = self.instruction;
	
	block = self.block;
	
	todo = [];
	
	if not block.is_critical:
		todo.append(BlockCruciality(block));
	
	def submit(valnum):
		enter(f"submit(valnum = {valnum})");
		
		if type(exp := block.expression_table.vntoex(valnum)) is Phi:
			if not exp.is_critical:
				for source in exp.sources:
					inst = source.valnum_to_instruction[valnum];
					dprint(f"inst: {inst}, source.rpo = {source.rpo}");
					todo.append(InstructionCruciality(inst, source));
				exp.is_critical = True;
		else:
			finger, inst = block, None;
			
			while (inst := finger.valnum_to_instruction.get(valnum)) is None:
				dprint(f"finger.rpo = {finger.rpo}");
				finger = finger.immedate_dominator;
				if finger == finger.immedate_dominator:
					break;
			
			if inst is not None and not inst.is_critical:
				dprint(f"pushed: {inst}");
				todo.append(InstructionCruciality(inst, finger));
			else:
				dprint(f"finger.rpo = {finger.rpo}");
				dprint(f"inst = {inst}");
				# assert(not "CHECK");
		
		exit("return;");
	
	if not inst.is_critical:
		dprint(f"inst: {inst}");
		match inst.op:
			case "loadI" | "ret":
				pass;
			
			case "iwrite" | "swrite" | "putchar"\
				| "cbrne" | "cbr" \
				| "load" | "fload" \
				| "i2i" | "f2i" | "i2f" | "iread" \
				| "iret":
				src, = inst.ins;
				submit(src);
			
			case "multI" | "addI" | "loadAI" | "rshiftI":
				inner, const = inst.ins;
				submit(inner);
			
			case "call" | "icall":
				for param in inst.ins:
					submit(param);
			
			case   "cbr_GT" | "cbr_GE" | "cbr_NE" | "cbr_EQ" | "cbr_LE" | "cbr_LT" \
				 | "cmp_GT" | "cmp_LT" | "cmp_GE" | "cmp_LE" | "sub"\
					| "loadAO" | "add" | "fadd" | "or" | "mult" | "fmult" | "mod":
				left, right = inst.ins;
				submit(left);
				submit(right);
			
			case "store":
				value, dest = inst.ins;
				submit(value);
				submit(dest);
			
			case "storeAI":
				value, base, offset = inst.ins;
				submit(value);
				submit(base);
			
			case "storeAO":
				value, base, index = inst.ins;
				submit(value);
				submit(base);
				submit(index);
			
			case _:
				assert(not "TODO");
		
		inst.is_critical = True;
	
#	if inst.out == 79:
#		dprint(f"inst.is_critical = {inst.is_critical}");
#		assert(not "CHECK");
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;

















