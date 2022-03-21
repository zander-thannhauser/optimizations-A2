
from debug import *;

def Instruction_init(self, op, ins, out):
	enter(f"Instruction.init(op = {op}, ins = {ins}, out = {out})");
	self.op = op;
	self.ins = ins;
	self.out = out;
	exit(f"return;");

