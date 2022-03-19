
from debug import *;

from .common import load_literal;

from ExpressionTable.Constant.self import Constant;

def optimize_mult(ops, et, ins, out):
	enter(f"optimize_mult(ins = {ins}, out = {out})");
	
	lvn, rvn = et.vrtovn(ins[0]), et.vrtovn(ins[1])
	
	match (et.vntoex(lvn), et.vntoex(rvn)):
		# constant-folding:
		case (Constant(value = a), Constant(value = b)):
			load_literal(ops, et, a * b, out);
			
		# identities:
		# 0 * X = 0
		case (Constant(value = 0), _):
			assert(not "TODO");
		# 1 * X = X
		case (Constant(value = 1), _):
			# avrwvn(out, rvn);
			assert(not "TODO");
		# X * 0 = 0
		case (_, Constant(value = 0)):
			assert(not "TODO");
		# X * 1 = X
		case (_, Constant(value = 1)):
			assert(not "TODO");
		
#		# substitutions:
#		# (addI X, a) * b => addI (multI X, b), (a * b)
#		case (("addI", X, a), b) if type(b) is int:
#			# check for using a move instruction's result
#			if oldgvn(X):
#				consider(ops, ("multI", lvn, b), out);
#			else:
#				subvn = consider(ops, ("multI", X, b));
#				consider(ops, ("addI", subvn, a * b), out);

#		# a * (addI X, b) => addI (multI X, a), (a * b)
#		case (a, ("addI", X, b)) if type(a) is int:
#			assert(not "TODO");

#		# (multI X, a) * b => multI X, (a * b)
#		case (("multI", X, a), b) if type(b) is int:
#			assert(not "TODO");

#		# a * (multI X, b) => multI X, (a * b)
#		case (a, ("multI", X, b)) if type(a) is int:
#			assert(not "TODO");

#		# (multI X, a) * (multI Y, b) => multI (mult X Y), (a * b)
#		case (("multI", X, a), ("multI", Y, b)):
#			assert(not "TODO");

#		# mult X, c => multI X, c:
#		case (_, c) if type(c) is int:
#			consider(ops, ("multI", lvn, c), out);

#		# mult c, X => multI X, c:
#		case (c, _) if type(c) is int:
#			consider(ops, ("multI", rvn, c), out);

#		# default:
		case (lex, rex):
			print(f"lex, rex = {lex}, {rex}");
			# consider(ops, ("mult", lvn, rvn), out);
			assert(not "TODO");
	
	
	exit("return;");





