
from debug import *;

from Instruction.self import Instruction;

from ExpressionTable.Expression.self import Expression;

def optimize_iret(ops, et, ins, out, label, volatile):
	enter(f"optimize_iwrite(ins = {ins}, out = {out})");
	
	ivn = et.vrtovn(ins[0]);
	
	ops.append(Instruction("iret", [ivn], None));
	
	exit("return");
