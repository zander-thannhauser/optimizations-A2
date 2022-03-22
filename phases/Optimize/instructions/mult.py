
from debug import *;

from .common import load_literal, consider;

from ExpressionTable.Constant.self import Constant;
from ExpressionTable.Expression.self import Expression;

def optimize_mult(ops, et, ins, out, label):
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
		# (addI X, a) * b => addI (multI X, b), (a * b)
		case (Expression(op = "addI", ins = [X, a]), Constant(value = b)):
			if a * b:
				subvn = consider(ops, et, "multI", (X, b));
				consider(ops, et, "addI", (subvn, a * b), out);
			else:
				assert(not "TODO");
		
		# a * (addI X, b) => addI (multI X, a), (a * b)
		case (Constant(value = a), Expression(op = "addI", ins = [X, b])):
			assert(not "TODO");
		
		# (multI X, a) * b => multI X, (a * b)
		case (Expression(op = "multI", ins = [X, a]), Constant(value = b)):
			consider(ops, et, "multI", (X, a * b), out);
		
		# a * (multI X, b) => multI X, (a * b)
		case (Constant(value = a), Expression(op = "multI", ins = [X, b])):
			assert(not "TODO");
		
		# (multI X, a) * (multI Y, b) => multI (mult X Y), (a * b)
		case (Expression(op = "multI", ins = [X, a]), \
				Expression(op = "multI", ins = [Y, b])):
			assert(not "TODO");
		
		# mult X, c => multI X, c:
		case (_, Constant(value = c)):
			consider(ops, et, "multI", (lvn, c), out);
		
		# mult c, X => multI X, c:
		case (Constant(value = c), _):
			consider(ops, et, "multI", (rvn, c), out);
		
#		# default:
		case (lex, rex):
			print(f"lex, rex = {lex}, {rex}");
			consider(ops, et, "mult", (lvn, rvn), out);
	
	
	exit("return;");



















