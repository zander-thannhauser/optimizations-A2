
from debug import *;

from .common import load_literal, consider;

from ExpressionTable.Constant.self import Constant;
from ExpressionTable.Expression.self import Expression;

def optimize_testle(ops, et, ins, out):
	enter(f"optimize_testle(ins = {ins}, out = {out})");
	
	ivn = et.vrtovn(ins[0]);
	
	match (et.vntoex(ivn)):
		# constant-fold:
		case Constant(value = c):
#			load_literal(ops, 1 if c == 0 else 0, out);
			assert(not "TODO");
		
		# substitutions:
		case Expression(op = "comp", ins = [X, Y]):
			consider(ops, et, "cmp_GT", (X, Y), out);
		
		# default:
		case (iex):
			assert(not "TODO");
	
	exit("return;");










