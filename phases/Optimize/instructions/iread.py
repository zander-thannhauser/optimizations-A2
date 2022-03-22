
from debug import *;

from Instruction.self import Instruction;

from ExpressionTable.Expression.self import Expression;

def optimize_iread(ops, et, ins, out, label):
	enter(f"optimize_iread(ins = {ins}, out = {out})");
	
	ivn = et.vrtovn(ins[0]);
	
	ops.append(Instruction("iread", [ivn], None));
	
	exit("return");
