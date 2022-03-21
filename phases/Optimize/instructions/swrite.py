
from debug import *;

from Instruction.self import Instruction;

from ExpressionTable.Expression.self import Expression;

def optimize_swrite(ops, et, ins, out, label):
	enter(f"optimize_swrite(ins = {ins}, out = {out})");
	
	ivn = et.vrtovn(ins[0]);
	
	ops.append(Instruction("swrite", [ivn], None));
	
	exit("return");
