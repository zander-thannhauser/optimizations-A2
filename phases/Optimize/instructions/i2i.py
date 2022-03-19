
from debug import *;

def optimize_i2i(ops, et, ins, out):
	enter(f"optimize_i2i(ins = {ins}, out = {out})");
	
	valnum = et.vrtovn(ins[0]);
	
	et.avrwvn(out, valnum);
	
	exit("return;");
