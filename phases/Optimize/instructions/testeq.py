
from debug import *;

from .common import load_literal, consider;

from ExpressionTable.Constant.self import Constant;
from ExpressionTable.Expression.self import Expression;

def optimize_testeq(ops, et, ins, out):
	enter(f"optimize_testeq(ins = {ins}, out = {out})");
	
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
					consider(ops, et, "not", (X, ), out);
				case _:
					# consider(ops, ("cmp_EQ", X, Y), out);
					assert(not "TODO");
					
		# default:
		case (iex):
			assert(not "TODO");
	
	exit("return;");










