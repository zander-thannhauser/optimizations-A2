
from debug import *;

from Instruction.self import Instruction;

from ExpressionTable.Expression.self import Expression;

def optimize_ret(ops, et, ins, out, label, volatile):
	enter(f"optimize_ret(ins = {ins}, out = {out})");
	
	ops.append(Instruction("ret", [], None));
	
	exit("return");
