
from debug import *;

from Instruction.self import Instruction;

from ExpressionTable.Expression.self import Expression;

def optimize_jumpI(ops, et, ins, out):
	enter(f"optimize_jumpI(ins = {ins}, out = {out})");
	
	ops.append(Instruction("jumpI", ins, None));
	
	exit("return");
