
from debug import *;

def Instruction_init(self, op, ins, out, label = None):
	enter(f"Instruction.init(op = {op}, ins = {ins}, out = {out})");
	
	self.op = op;
	self.ins = ins;
	self.out = out;
	self.label = label; # for branch instructions
	
	self.is_critical = False;
	
	self.acting_i2i = False;
	
	exit(f"return;");

