
from debug import *;

from ExpressionTable.Constant.self import Constant;
from ExpressionTable.Expression.self import Expression;

from .common import load_literal;
from .common import consider;
from .add import optimize_add_vr;

def optimize_sub_vr(ops, et, lvn, rvn, out = None):
	enter(f"optimize_sub_vr(lvn = {lvn}, rvn = {rvn}, out = {out})");
	
	match (et.vntoex(lvn), et.vntoex(rvn)):
		
		# constant-folding:
		case (Constant(value = a), Constant(value = b)):
			retval = load_literal(ops, et, a - b, out);
		
		# identities:
		# X - 0 = X
		case (_, Constant(value = 0)):
			retval = et.avrwvn(out, lvn);
		
		case (Constant(value = 0), _):
			assert(not "TODO");
		
		# X - X = 0
		case (_, _) if lvn == rvn:
			assert(not "TODO");
#		
		# substitutions:
		# (addI X, a) - b => addI X, (a - b)
		case (Expression(op = "addI", ins = [X, a]), Constant(value = b)):
			if a - b == 0:
				retval = et.avrwvn(out, X);
			else:
				retval = consider(ops, et, "addI", (X, a - b), out);
		
		# a - (addI X, b) => sub (a - b), X
		case (Constant(value = a), Expression(op = "addI", ins = [X, b])):
			assert(not "TODO");
		
		# (add X, Y) - (add Z, Y) => X - Z
		case (Expression(op = "add", ins = [A, B]), \
			  Expression(op = "add", ins = [C, D])) if B == D:
			assert(not "TODO");
		
		# (add X, Y) - Y => X
		case (Expression(op = "add", ins = [X, Y]), _) if Y == rvn:
			assert(not "TODO");
		
		# (sub X, Y) - X => Y
		case (Expression(op = "sub", ins = [X, Y]), _) if X == rvn:
			assert(not "TODO");
		
		# (addI X, a) - (addI Y, b) => addI (sub X, Y), (a - b)
		case (Expression(op = "addI", ins = [X, a]), Expression(op = "addI", ins = [Y, b])):
			if X == Y:
#				assert(not "TODO");
				assert(not "TODO");
			elif a - b == 0:
				retval = optimize_sub_vr(ops, et, X, Y, out);
			else:
				subvn = optimize_sub_vr(ops, et, X, Y);
				retval = consider(ops, et, "addI", (subvn, a - b), out);
		
		# (multI X, a) - (multI Y, a) = multI (sub X, Y), a
		case (Expression(op = "multI", ins = [X, a]), \
			  Expression(op = "multI", ins = [Y, b])) if a == b:
			assert(not "TODO");
		
		# (addI X, a) - (multI Y, b) = (Y * -b + X) + a
		case (Expression(op = "addI",  ins = [X, a]), \
			  Expression(op = "multI", ins = [Y, b])):
			subvn1 = consider(ops, et, "multI", (Y, -b));
			subvn2 = optimize_add_vr(ops, et, X, subvn1);
			retval = consider(ops, et, "addI", (subvn2, a), out);
		
		# X - (addI Y, a) = (sub X, Y) - a
		case (_, Expression(op = "addI", ins = [Y, b])):
			subvn = optimize_sub_vr(ops, et, lvn, Y, out);
			retval = consider(ops, et, "addI", (subvn, -b), out);
		
		# X - (multI Y, a) = X + (multI Y, -a)
		case (_, Expression(op = "multI", ins = [Y, b])):
			subvn = consider(ops, et, "multI", (Y, -b));
			retval = optimize_add_vr(ops, et, lvn, subvn, out);
		
		# X - c => addI X, -c
		case (_, Constant(value = c)):
			retval = consider(ops, et, "addI", (lvn, -c), out);
		
		# default:
		case (lex, rex):
			dprint(f"lex, rex = {str(lex), str(rex)}");
			# consider(ops, ("sub", lvn, rvn), out);
			assert(not "TODO");
	
	exit(f"return {retval};");
	return retval;


def optimize_sub(ops, et, ins, out, label):
	enter(f"optimize_sub(ins = {ins}, out = {out})");
	
	lvn, rvn = et.vrtovn(ins[0]), et.vrtovn(ins[1])
	
	optimize_sub_vr(ops, et, lvn, rvn, out);
	
	exit("return;");



















