
from debug import *;

from .common import load_literal, consider;

#from ExpressionTable.Constant.self import Constant;
#from ExpressionTable.Expression.self import Expression;

def optimize_fmult(ops, et, ins, out, label):
	enter(f"optimize_fmult(ins = {ins}, out = {out})");
	
	lvn, rvn = et.vrtovn(ins[0]), et.vrtovn(ins[1])
	
	consider(ops, et, "fmult", (lvn, rvn), out);
	
	exit("return;");



















