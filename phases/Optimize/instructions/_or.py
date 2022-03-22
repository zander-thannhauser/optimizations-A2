
from debug import *;

from ExpressionTable.Constant.self import Constant;
from ExpressionTable.Expression.self import Expression;

from .common import consider;
from .common import load_literal;

def optimize_or_vr(ops, et, lvn, rvn, out = None):
	enter(f"optimize_or_vr(lvn = {lvn}, rvn = {rvn}, out = {out})");
	
	match (et.vntoex(lvn), et.vntoex(rvn)):
		# constant-folding:
		case (Constant(value = a), Constant(value = b)):
			retval = load_literal(ops, et, a + b, out);
		
		# identities:
		# zero or X = X
		case (Constant(value = 0), _):
			assert(not "TODO");
		
		# nonzero or X = nonzero
		case (Constant(value = a), _):
			assert(not "TODO");
		
		# X or 0 = X
		case (_, Constant(value = 0)):
			assert(not "TODO");
		
		# X or nonzero = nonzero
		case (_, Constant(value = b)):
			assert(not "TODO");
		
		# default:
		case (_, _):
			retval = consider(ops, et, "or", (lvn, rvn), out);
	
	exit(f"return {retval};");
	return retval;


def optimize_or(ops, et, ins, out, label):
	enter(f"optimize_or(ins = {ins}, out = {out})");
	
	lvn, rvn = et.vrtovn(ins[0]), et.vrtovn(ins[1])
	
	optimize_or_vr(ops, et, lvn, rvn, out);
	
	exit("return;");













