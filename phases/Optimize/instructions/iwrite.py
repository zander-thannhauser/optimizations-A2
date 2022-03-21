
from debug import *;

from Instruction.self import Instruction;

from ExpressionTable.Expression.self import Expression;

def optimize_iwrite(ops, et, ins, out, label):
	enter(f"optimize_iwrite(ins = {ins}, out = {out})");
	
	ivn = et.vrtovn(ins[0]);
	
	ops.append(Instruction("iwrite", [ivn], None));
	
	exit("return");
