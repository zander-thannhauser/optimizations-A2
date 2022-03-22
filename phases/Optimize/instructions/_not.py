
from debug import *;

from .common import consider;

from ExpressionTable.Expression.self import Expression;

def optimize_not_vr(ops, et, ivn, out):
	enter(f"optimize_not_vr(ivn = {ivn}, out = {out});");
	
	match (et.vntoex(ivn)):
		
		case Expression(op = "not"):
			assert(not "TODO");
		
#		case Expression(op = "or"):
#			assert(not "TODO");
#		
#		case Expression(op = "and"):
#			assert(not "TODO");
#		
		case Expression(op = "add"):
			# not(or())
			assert(not "TODO");
		
		case Expression(op = "sub"):
			# are they equal?
			assert(not "TODO");
		
		case Expression(op = "mult"):
			# not(and())
			assert(not "TODO");
		
		case (iex):
			dprint(f"iex = {iex}");
			retval = consider(ops, et, "not", (ivn,), out);
	
	exit(f"return {retval};");
	return retval;

