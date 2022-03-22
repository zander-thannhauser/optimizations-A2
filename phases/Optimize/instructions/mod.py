
from debug import *;

from .common import load_literal, consider;

from ExpressionTable.Constant.self import Constant;
from ExpressionTable.Expression.self import Expression;

def optimize_mod(ops, et, ins, out, label):
	enter(f"optimize_mod(ins = {ins}, out = {out})");
	
	lvn, rvn = et.vrtovn(ins[0]), et.vrtovn(ins[1])
	
	match (et.vntoex(lvn), et.vntoex(rvn)):
		# constant-folding:
		case (Constant(value = a), Constant(value = b)) if b != 0:
			load_literal(ops, et, a % b, out);
			
		# identities:
		# 0 % X = 0
		case (Constant(value = 0), _):
			assert(not "TODO");
		
#		# default:
		case (lex, rex):
			print(f"lex, rex = {lex}, {rex}");
			consider(ops, et, "mod", (lvn, rvn), out);
	
	
	exit("return;");



















