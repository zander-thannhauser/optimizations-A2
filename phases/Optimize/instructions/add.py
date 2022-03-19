
from debug import *;

from ExpressionTable.Constant.self import Constant;
from ExpressionTable.Expression.self import Expression;

from .common import consider;
from .common import load_literal;

def optimize_add(ops, et, ins, out):
	enter(f"optimize_add(ins = {ins}, out = {out})");
	
	lvn, rvn = et.vrtovn(ins[0]), et.vrtovn(ins[1])
	
	match (et.vntoex(lvn), et.vntoex(rvn)):
		# constant-folding:
		case (Constant(value = a), Constant(value = b)):
			load_literal(ops, et, a + b, out);
		
		# identities:
		# 0 + X = X
		case (Constant(value = 0), _):
			assert(not "TODO");
		
		# X + 0 = X
		case (_, Constant(value = 0)):
			assert(not "TODO");
		
#		# substitutions:
#		# (addI X, a) + b => addI X, (a + b)
		case (Expression(op = "addI", ins = [X, a]), Constant(value = b)):
#			# check for using a move instruction's result
#			if oldgvn(X):
#				consider(ops, ("addI", lvn, b), out);
#			elif a == -b:
#				assert(not "TODO");
#			else:
#				assert(not "TODO");
			assert(not "TODO");
		
		# a + (addI X, b) => addI X, (a + b)
		case (Constant(value = a), Expression(op = "addI", ins = [X, b])):
			# check for using a move instruction's result
			assert(not "TODO");
		
#		# (sub X, Y) + Y => X
		case (Expression(op = "sub", ins = [X, Y]), _) if Y == rvn:
			assert(not "TODO");
		
		# X + (sub Y, X) => Y
		case (_, Expression(op = "sub", ins = [Y, Z])) if lvn == Z:
			assert(not "TODO");
		
		# (addI X, a) + (addI, Y, b) => addI (add X, Y), (a + b)
		case (Expression(op = "addI", ins = [X, a]), \
			  Expression(op = "addI", ins = [Y, b])):
			# check for using a move instruction's result
			if a + b == 0:
				assert(not "TODO");
			else:
				assert(not "TODO");
		
		# (multI X, a) + (multI Y, a) = multI (add X, Y), a
		case (Expression(op = "multI", ins = [X, a]), \
			 (Expression(op = "multI", ins = [Y, b]))) \
			if a == b:
				# check for using a move instruction's result
				assert(not "TODO");
		
		# X + c => addI X, c
		case (_, Constant(value = c)):
			consider(ops, et, "addI", (lvn, c), out);
		
		# c + X => addI X, c
		case (Constant(value = c), _):
			# consider(ops, ("addI", rvn, lex), out);
			assert(not "TODO");
		
		# default:
		case (_, _):
			# consider(ops, ("add", lvn, rvn), out);
			assert(not "TODO");
	
	exit("return;");













