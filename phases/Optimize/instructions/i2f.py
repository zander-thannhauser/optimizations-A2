
from debug import *;

#from ExpressionTable.Constant.self import Constant;
#from ExpressionTable.Expression.self import Expression;

from .common import consider;
#from .common import load_literal;

def optimize_i2f_vr(ops, et, ivn, out = None):
	enter(f"optimize_i2f_vr(ivn = {ivn}, out = {out})");
	
	retval = consider(ops, et, "i2f", (ivn, ), out);
	
	exit(f"return {retval};");
	return retval;


def optimize_i2f(ops, et, ins, out, label):
	enter(f"optimize_i2f(ins = {ins}, out = {out})");
	
	ivn = et.vrtovn(ins[0])
	
	optimize_i2f_vr(ops, et, ivn, out);
	
	exit("return;");













