
from debug import *;

from Instruction.self import Instruction;

from ExpressionTable.Expression.self import Expression;

def optimize_call(ops, et, ins, out, label):
	enter(f"optimize_call(ins = {ins}, out = {out})");
	
	pvns = [et.vrtovn(i) for i in ins];
	
	ops.append(Instruction("call", pvns, None, label));
	
	exit("return");
