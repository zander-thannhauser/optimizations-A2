
from debug import *;

from .common import load_literal;
from .common import consider;

from ExpressionTable.Constant.self import Constant;
from ExpressionTable.Expression.self import Expression;

def optimize_sub(ops, et, ins, out):
	enter(f"optimize_sub(ins = {ins}, out = {out})");
	
	lvn, rvn = et.vrtovn(ins[0]), et.vrtovn(ins[1])
	
	match (et.vntoex(lvn), et.vntoex(rvn)):
		
		# constant-folding:
		case (Constant(value = a), Constant(value = b)):
			load_literal(ops, et, a - b, out);
		
		# identities:
		# X - 0 = X
		case (_, Constant(value = 0)):
			et.avrwvn(out, lvn);
		
		# X - X = 0
		case (_, _) if lvn == rvn:
			assert(not "TODO");
#		
		# substitutions:
		# (addI X, a) - b => addI X, (a - b)
		case (Expression(op = "addI", ins = [X, a]), Constant(value = b)):
			if a == b:
				# avrwvn(out, X);
				assert(not "TODO");
			else:
				consider(ops, et, "addI", (X, a - b), out);
		
		# a - (addI X, b) => sub (a - b), X
		case (Constant(value = a), Expression(op = "addI", ins = [X, b])):
			assert(not "TODO");
		
		# (add X, Y) - Y => X
		case (Expression(op = "add", ins = [X, Y]), _) if Y == rvn:
			assert(not "TODO");
		
		# (sub X, Y) - X => Y
		case (Expression(op = "sub", ins = [X, Y]), _) if X == rvn:
			assert(not "TODO");
		
		# (addI X, a) - (addI Y, b) => addI (sub X, Y), (a - b)
		case (Expression(op = "addI", ins = [X, a]), Expression(op = "addI", ins = [Y, b])):
#			# check for using a move instruction's result
#			if oldgvn(X) or oldgvn(Y):
#				assert(not "TODO");
#			elif X == Y:
#				assert(not "TODO");
#			elif a == b:
#				consider(ops, ("sub", X, Y), out);
#			else:
#				subvn = consider(ops, ("sub", X, Y));
#				consider(ops, ("addI", subvn, a - b), out);
			assert(not "TODO");
		
		# (multI X, a) - (multI Y, a) = multI (sub X, Y), a
		case (Expression(op = "multI", ins = [X, a]), Expression(op = "multI", ins = [Y, b])) if a == b:
			assert(not "TODO");
		
		# X - c => addI X, -c
		case (_, c) if type(c) is int:
			# consider(ops, ("addI", lvn, -c), out);
			assert(not "TODO");
		
		# default:
		case (lex, rex):
			dprint(f"lex, rex = {str(lex), str(rex)}");
			# consider(ops, ("sub", lvn, rvn), out);
			assert(not "TODO");
	
	exit("return;");



















