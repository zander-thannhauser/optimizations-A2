
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
			assert(not "TODO");
		
		# store (sub X, ("multI", Y, c)) => Z === storeAO X, (multI, Y -c) => Z
		case Expression(op = "sub", ins = [X, Y]):
			assert(not "TODO");
			# check for using a move instruction's result
#			if     (X != "%vr0" and X in vrtogvn_lookup.values()) \
#				or (Y != "%vr0" and Y in vrtogvn_lookup.values()):
#				ops.append(("store", [ivn], "=>", [ovn]));
#			else:
#				subex = vntoex(Y);
#				if subex[0] == "multI":
#					subvn = consider(ops, ("multI", subex[1], -subex[2]));
#					ops.append(("storeAO", [ivn], "=>", [X, subvn]));
#				elif subex[0] == "sub":
#					assert(not "TODO");
#				else:
#					ops.append(("store", [ivn], "=>", [ovn]));
		
		# default:
		case (oexp):
			dprint(f"oexp == {oexp}");
			assert(not "TODO");
#			ops.append(("store", [ivn], "=>", [ovn]));
	
	# apexwvn(ovn, ivn);
	# assert(not "TODO");

	exit("return;");






