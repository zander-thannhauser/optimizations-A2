
from debug import *;

from Instruction.self import Instruction;

from ExpressionTable.Expression.self import Expression;

def optimize_fload(ops, et, ins, out, label):
	enter(f"optimize_fload(ins = {ins}, out = {out})");
	
	ivn = et.vrtovn(ins[0]);
	
	ovn = et.mkvn();
	
	match (et.vntoex(ivn)):
		# fload (addI X, c) => Y === floadAI X, c => Y
		case Expression(op = "addI", ins = [X, c]):
			# ops.append(Instruction("floadAI", [X, c], ovn));
			assert(not "TODO");
		
		# fload (add  X, Y) => Z === floadAO X, Y => Z
		case Expression(op = "add", ins = [X, Y]):
			# ops.append(Instruction("floadAO", [X, Y], ovn));
			assert(not "TODO");
		
		case iex:
			dprint(f"iex = {iex}");
			ops.append(Instruction("fload", [ivn], ovn));
	
	et.avrwvn(out, ovn);
	
	exit("return");
