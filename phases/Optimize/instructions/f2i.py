
from debug import *;

#from ExpressionTable.Constant.self import Constant;
#from ExpressionTable.Expression.self import Expression;

from .common import consider;
#from .common import load_literal;

def optimize_f2i_vr(ops, et, ivn, out = None):
	enter(f"optimize_f2i_vr(ivn = {ivn}, out = {out})");
	
	retval = consider(ops, et, "f2i", (ivn, ), out);
	
	exit(f"return {retval};");
	return retval;


def optimize_f2i(ops, et, ins, out, label):
	enter(f"optimize_f2i(ins = {ins}, out = {out})");
	
	ivn = et.vrtovn(ins[0])
	
	optimize_f2i_vr(ops, et, ivn, out);
	
	exit("return;");













