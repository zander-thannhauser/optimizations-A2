
from debug import *;

from .common import load_literal, consider;

from ExpressionTable.Constant.self import Constant;
from ExpressionTable.Expression.self import Expression;

def optimize_rshift(ops, et, ins, out, label):
	enter(f"optimize_rshift(ins = {ins}, out = {out})");
	
	lvn, rvn = et.vrtovn(ins[0]), et.vrtovn(ins[1])
	
	match (et.vntoex(lvn), et.vntoex(rvn)):
		# constant-folding:
		case (Constant(value = a), Constant(value = b)):
			# load_literal(ops, et, a * b, out);
			assert(not "TODO");
			
		# identities:
		# 0 >> X = 0
		case (Constant(value = 0), _):
			assert(not "TODO");
		# X >> 0 = X
		case (_, Constant(value = 0)):
			assert(not "TODO");
		
		# rshift X, c => rshiftI X, c:
		case (_, Constant(value = c)):
			consider(ops, et, "rshiftI", (lvn, c), out);
		
		# default:
		case (lex, rex):
			print(f"lex, rex = {lex}, {rex}");
			# consider(ops, et, "mult", (lvn, rvn), out);
			assert(not "TODO");
	
	
	exit("return;");



















