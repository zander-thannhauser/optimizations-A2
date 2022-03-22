
from debug import *;

from .common import load_literal;

from Instruction.self import Instruction;

from ExpressionTable.Expression.self import Expression;
from ExpressionTable.Constant.self import Constant;

def optimize_store(ops, et, ins, out, label):
	enter(f"optimize_store(ins = {ins}, out = {out})");
	
	ivn = et.vrtovn(ins[0]);
	ovn = et.vrtovn(ins[1]);
	
	match (et.vntoex(ovn)):
		# store X, (Y + c) => storeAI X -> Y, c
		case Expression(op = "addI", ins = [X, c]):
			ops.append(Instruction("storeAI", [ivn, X, c], None));
		
		# store X, (Y + Z) => storeAO X -> Y, Z
		case Expression(op = "add", ins = [X, Y]):
			ops.append(Instruction("storeAO", [ivn, X, Y], None));
		
		# default:
		case (oexp):
			dprint(f"oexp == {oexp}");
			assert(not "TODO");
#			ops.append(("store", [ivn], "=>", [ovn]));
	
	# apexwvn(ovn, ivn);
	# assert(not "TODO");

	exit("return;");






