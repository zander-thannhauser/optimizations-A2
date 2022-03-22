
from debug import *;

from .common import load_literal, consider;

from ExpressionTable.Constant.self import Constant;
from ExpressionTable.Expression.self import Expression;

def optimize_testlt(ops, et, ins, out, label):
	enter(f"optimize_testlt(ins = {ins}, out = {out})");
	
	ivn = et.vrtovn(ins[0]);
	
	match (et.vntoex(ivn)):
		# constant-fold:
		case Constant(value = c):
			load_literal(ops, et, 1 if c < 0 else 0, out);
		
		# substitutions:
		case Expression(op = "comp", ins = [X, Y]):
			consider(ops, et, "cmp_LT", (X, Y), out);
		
		# default:
		case (iex):
			assert(not "TODO");
	
	exit("return;");










