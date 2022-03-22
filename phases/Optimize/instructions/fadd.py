
from debug import *;

from .common import load_literal, consider;

#from ExpressionTable.Constant.self import Constant;
#from ExpressionTable.Expression.self import Expression;

def optimize_fadd(ops, et, ins, out, label):
	enter(f"optimize_fadd(ins = {ins}, out = {out})");
	
	lvn, rvn = et.vrtovn(ins[0]), et.vrtovn(ins[1])
	
	consider(ops, et, "fadd", (lvn, rvn), out);
	
	exit("return;");



















