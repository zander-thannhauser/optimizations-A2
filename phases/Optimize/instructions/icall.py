
from debug import *;

from Instruction.self import Instruction;

from ExpressionTable.Expression.self import Expression;

def optimize_icall(ops, et, ins, out, label):
	enter(f"optimize_icall(ins = {ins}, out = {out})");
	
	pvns = [et.vrtovn(i) for i in ins];
	
	ovn = et.mkvn();
	
	ops.append(Instruction("icall", pvns, ovn, label));
	
	et.avrwvn(out, ovn);
	
	exit("return");
