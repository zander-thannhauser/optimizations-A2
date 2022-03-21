
from debug import *;

from .common import load_literal, consider;

from ExpressionTable.Constant.self import Constant;
from ExpressionTable.Expression.self import Expression;

def optimize_testne(ops, et, ins, out, label):
	enter(f"optimize_testne(ins = {ins}, out = {out})");
	
	ivn = et.vrtovn(ins[0]);
	
	match (et.vntoex(ivn)):
		# constant-fold:
		case Constant(value = c):
#			load_literal(ops, 1 if c == 0 else 0, out);
			assert(not "TODO");
		
		# substitutions:
		case Expression(op = "comp", ins = [X, Y]):
			# check for using a move instruction's result
			match (et.vntoex(X), et.vntoex(Y)):
				case (Constant(value = 0), _):
					assert(not "TODO");
				case (_, Constant(value = 0)):
					et.avrwvn(out, X);
				case _:
					consider(ops, et, "cmp_EQ", (X, Y), out);
					
		# default:
		case (iex):
			assert(not "TODO");
	
	exit("return;");










