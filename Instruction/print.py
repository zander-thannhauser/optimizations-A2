
from debug import *;

from ExpressionTable.Constant.self import Constant;

def Instruction_print(self, p):
	# knows which arrows go to which commands
	match self.op:
		
		case "loadI":
			match (self.ins[0]):
				case Constant(value = c):
					    p.printf("loadI   %i             -> %%vr%i", c, self.out);
				case str() as s:
					    p.printf("loadI   %s             -> %%vr%i", s, self.out);
				case _:
					assert(not "TODO");
		
		case "addI":    p.printf("addI    %%vr%i, %i     => %%vr%i", *self.ins, self.out);
		case "multI":   p.printf("multI   %%vr%i, %i     => %%vr%i", *self.ins, self.out);
		
		case "add":     p.printf("add     %%vr%i, %%vr%i => %%vr%i", *self.ins, self.out);
		
		case "loadAI":  p.printf("loadAI  %%vr%i, %i     => %%vr%i", *self.ins, self.out);
		case "loadAO":  p.printf("loadAO  %%vr%i, %%vr%i => %%vr%i", *self.ins, self.out);
		
		case "storeAI": p.printf("storeAI %%vr%i         => %%vr%i,     %i", *self.ins);
		case "storeAO": p.printf("storeAO %%vr%i         => %%vr%i, %%vr%i", *self.ins);
		
		case "i2i":     p.printf("i2i     %%vr%i         => %%vr%i", *self.ins, self.out);
		
		case "cmp_LE":  p.printf("cmp_LE  %%vr%i, %%vr%i => %%vr%i", *self.ins, self.out);
		
		case "cbr":     p.printf("cbr     %%vr%i         -> %s", *self.ins, self.label);
		case "cbrne":   p.printf("cbrne   %%vr%i         -> %s", *self.ins, self.label);
		case "cbr_GT":  p.printf("cbr_GT  %%vr%i, %%vr%i -> %s", *self.ins, self.label);
		case "cbr_NE":  p.printf("cbr_NE  %%vr%i, %%vr%i -> %s", *self.ins, self.label);
		case "cbr_GE":  p.printf("cbr_GE  %%vr%i, %%vr%i -> %s", *self.ins, self.label);
		case "cbr_EQ":  p.printf("cbr_EQ  %%vr%i, %%vr%i -> %s", *self.ins, self.label);
		case "cbr_LE":  p.printf("cbr_LE  %%vr%i, %%vr%i -> %s", *self.ins, self.label);
		
		case "ret":     p.printf("ret");
		
		case "iwrite":  p.printf("iwrite  %%vr%i              ", *self.ins);
		case "swrite":  p.printf("swrite  %%vr%i              ", *self.ins);
		
		case _:
			dprint(f"self.op == {self.op}");
			assert(not "TODO");
