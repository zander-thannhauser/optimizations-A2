
from debug import *;

from Instruction.self import Instruction;

from ExpressionTable.Expression.self import Expression;

def optimize_load(ops, et, ins, out):
	enter(f"optimize_load(ins = {ins}, out = {out})");
	
	ivn = et.vrtovn(ins[0]);
	
	ovn = et.mkvn();
	
	match (et.vntoex(ivn)):
		# load (addI X, c) => Y === loadAI X, c => Y
		case Expression(op = "addI", ins = [X, c]):
			ops.append(Instruction("loadAI", [X, c], ovn));
		
		# load (add  X, Y) => Z === loadAO X, Y => Z
		case Expression(op = "add", ins = [X, Y]):
			assert(not "CHECK");
		
		# load (sub X, ("multI", Y, c)) => Z === loadAO X, (multI, Y -c) => Z
		case Expression(op = "sub", ins = [X, Y]):
#			# check for using a move instruction's result
#			if oldgvn(X):
#				assert(not "TODO");
#			else:
#				subex = vntoex(Y);
#				if subex[0] == "multI":
#					subvn = consider(ops, ("multI", subex[1], -subex[2]));
#					ops.append(("loadAO", [X, subvn], "=>", [ovn]));
#				elif subex[0] == "sub":
#					assert(not "TODO");
#				else:
#					assert(not "TODO");
			assert(not "TODO");
		
		case iex:
			dprint(f"iex = {iex}");
#			ops.append(("load", [ivn], "=>", [ovn]));
#			apexwvn(ivn, ovn);
			assert(not "TODO");
	
	et.avrwvn(out, ovn);
	
	exit("return");
