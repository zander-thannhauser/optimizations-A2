
from debug import *;

from ExpressionTable.Constant.self import Constant;
from ExpressionTable.Expression.self import Expression;

from .common import consider;
from .common import load_literal;

def optimize_comp(ops, et, ins, out):
	enter(f"optimize_comp(ins = {ins}, out = {out})");
	
	lvn, rvn = et.vrtovn(ins[0]), et.vrtovn(ins[1])
	
	match (et.vntoex(lvn), et.vntoex(rvn)):
		
		# constant-fold:
		case (Constant(value = a), Constant(value = b)):
			# load_literal(ops, comp(lex, rex), out);
			assert(not "TODO");
		
		# identities:
		# comp(X, X) = 0
		case (_, _) if lvn == rvn:
			assert(not "TODO");
		
		# substitutions:
		# (addI X, a) vs b => X vs (b - a)
		case (Expression(op = "addI", ins = [X, a]), Constant(value = b)):
#			# check for using a move instruction's result
#			if oldgvn(X):
#				consider(ops, ("comp", lvn, rvn), out);
#			else:
#				subvn = load_literal(ops, b - a);
#				consider(ops, ("comp", X, subvn), out);
			assert(not "TODO");
		
		# (addI X, a) vs (addI X, b) => a vs b
		case (Expression(op = "addI", ins = [X, a]), \
			  Expression(op = "addI", ins = [Y, b])) if X == Y:
			assert(not "TODO");
		
		# (addI X, a) vs (addI Y, b) => X vs (addI Y, b - a)
		case (Expression(op = "addI", ins = [X, a]), \
			  Expression(op = "addI", ins = [Y, b])):
			if a == b:
				# after you've canceled the adds on both sides,
				# is the inner expression a multiply?
				# if so: try to cancel those factors
				assert(not "TODO");
			else:
				# or whichever's lower
				assert(not "TODO");
		
		# (multI X, a) vs (multI X, b) => a vs b
		case (Expression(op = "multI", ins = [X, a]), \
			  Expression(op = "multI", ins = [Y, b])) if X == Y:
			assert(not "TODO");
		
		# (multI X, a) vs (multI Y, a) => X vs Y
		case (Expression(op = "multI", ins = [X, a]), \
			  Expression(op = "multI", ins = [Y, b])) if a == b:
			assert(not "TODO");
		
		# (multI X, a) vs b => X vs b // a
		case (Expression(op = "multI", ins = [X, a]), Constant(value = b)):
			if b % a == 0:
				assert(not "TODO");
			else:
				assert(not "TODO");
		
		# (multI X, a) vs (multI Y, b) => (multI X, (a // b)) vs Y
		case (Expression(op = "multI", ins = [X, a]), \
			  Expression(op = "multI", ins = [Y, b])) \
			  if a % b == 0 or b % a == 0:
			# or whichever's lower
			assert(not "TODO");
		
		case (Expression(op = "mult", ins = [A, B]), Expression(op = "mult", ins = [C, D])) if A == C:
			assert(not "TODO");
		
		case (Expression(op = "mult", ins = [A, B]), Expression(op = "mult", ins = [C, D])) if B == D:
			assert(not "TODO");
		
		case (Expression(op = "multI", ins = [X, a]), Constant(value = b)):
			assert(not "TODO");
		
		case (Constant(value = b), Expression(op = "multI", ins = [X, a])):
			assert(not "TODO");
		
		case (Expression(op = "sub", ins = [X, Y]), Constant(value = c)):
			# if Y is an addI, then you can bring it across
			assert(not "TODO");
		
		case (Expression(op = "sub", ins = [X, Y]), Constant(value = 0)):
			assert(not "TODO");
		
		case (Constant(value = 0), Expression(op = "sub", ins = [X, a])):
			assert(not "TODO");
		
		case (Expression(op = "sub", ins = [A, B]), Expression(op = "sub", ins = [C, D])) if B == D:
			assert(not "TODO");
		
		case (Expression(op = "add", ins = [A, B]), Expression(op = "add", ins = [C, D])) if A == C:
			assert(not "TODO");
		
		case (Expression(op = "add", ins = [A, B]), Expression(op = "add", ins = [C, D])) if B == D:
			assert(not "TODO");
		
		case (Expression(op = "addI", ins = [X, a]), Constant(value = b)):
			assert(not "TODO");
		
		case (Constant(value = b), Expression(op = "addI", ins = [X, a])):
			assert(not "TODO");
		
		# default:
		case (lex, rex):
			dprint(f"lex, rex = {lex}, {rex}");
			consider(ops, et, "comp", (lvn, rvn), out);
		
	exit("return;");



















