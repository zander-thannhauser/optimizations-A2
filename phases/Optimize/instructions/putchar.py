
from debug import *;

from Instruction.self import Instruction;

from ExpressionTable.Expression.self import Expression;

def optimize_putchar(ops, et, ins, out, label):
	enter(f"optimize_putchar(ins = {ins}, out = {out})");
	
	ivn = et.vrtovn(ins[0]);
	
	ops.append(Instruction("putchar", [ivn], None));
	
	exit("return");
