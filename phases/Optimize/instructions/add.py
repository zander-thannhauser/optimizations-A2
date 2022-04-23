
from debug import *;

from ExpressionTable.Constant.self import Constant;
from ExpressionTable.Expression.self import Expression;

from .common import consider;
from .common import load_literal;

def optimize_add_vr(ops, et, lvn, rvn, out = None):
	enter(f"optimize_add_vr(lvn = {lvn}, rvn = {rvn}, out = {out})");
	
	match (et.vntoex(lvn), et.vntoex(rvn)):
		# constant-folding:
		case (Constant(value = a), Constant(value = b)):
			retval = load_literal(ops, et, a + b, out);
		
		# identities:
		# 0 + X = X
		case (Constant(value = 0), _):
			assert(not "TODO");
		
		# X + 0 = X
		case (_, Constant(value = 0)):
			assert(not "TODO");
		
		# substitutions:
		# (addI X, a) + b => addI X, (a + b)
		case (Expression(op = "addI", ins = [X, a]), Constant(value = b)):
			if a + b == 0:
				assert(not "TODO");
			else:
				retval = consider(ops, et, "addI", (X, a + b), out);
		
		# a + (addI X, b) => addI X, (a + b)
		case (Constant(value = a), Expression(op = "addI", ins = [X, b])):
			if a + b == 0:
				assert(not "TODO");
			else:
				retval = consider(ops, et, "addI", (X, a + b), out);
		
#		# (sub X, Y) + Y => X
		case (Expression(op = "sub", ins = [X, Y]), _) if Y == rvn:
			assert(not "TODO");
		
		# X + (sub Y, X) => Y
		case (_, Expression(op = "sub", ins = [Y, Z])) if lvn == Z:
			assert(not "TODO");
		
		# (addI X, a) + (addI, Y, b) => addI (add X, Y), (a + b)
		case (Expression(op = "addI", ins = [X, a]), \
			  Expression(op = "addI", ins = [Y, b])):
			if a + b == 0:
				assert(not "TODO");
			else:
				subvn = optimize_add_vr(ops, et, X, Y);
				retval = consider(ops, et, "addI", (subvn, a + b), out);
		
		# (multI X, a) + (multI, Y, a) => multI (add X, Y), a
		case (Expression(op = "multI", ins = [X, a]), \
			  Expression(op = "multI", ins = [Y, b])):
			assert(not "TODO");
		
		# (addI X, a) + Y => addI (add X, Y), a
		case (Expression(op = "addI", ins = [X, a]), _):
			subvn = optimize_add_vr(ops, et, X, rvn);
			retval = consider(ops, et, "addI", (subvn, a), out);
		
		# X + (addI Y, a) => addI (add X, Y), a
		case (_, Expression(op = "addI", ins = [Y, a])):
			subvn = optimize_add_vr(ops, et, lvn, Y);
			retval = consider(ops, et, "addI", (subvn, a), out);
		
		# (multI X, a) + (multI Y, a) = multI (add X, Y), a
		case (Expression(op = "multI", ins = [X, a]), \
			 (Expression(op = "multI", ins = [Y, b]))) \
			if a == b:
				# check for using a move instruction's result
				assert(not "TODO");
		
		# X + c => addI X, c
		case (_, Constant(value = c)):
			retval = consider(ops, et, "addI", (lvn, c), out);
		
		# c + X => addI X, c
		case (Constant(value = c), _):
			retval = consider(ops, et, "addI", (rvn, c), out);
		
		# default:
		case (_, _):
			retval = consider(ops, et, "add", (lvn, rvn), out);
	
	exit(f"return {retval};");
	return retval;


def optimize_add(ops, et, ins, out, label):
	enter(f"optimize_add(ins = {ins}, out = {out})");
	
	lvn, rvn = et.vrtovn(ins[0]), et.vrtovn(ins[1])
	
	optimize_add_vr(ops, et, lvn, rvn, out);
	
	exit("return;");













