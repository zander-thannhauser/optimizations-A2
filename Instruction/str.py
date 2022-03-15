
def Instruction_str(self):
	out = self.operation;
	out += " " + ', '.join(self.ins);
	if self.outs:
		out += " => " + ', '.join(self.outs);
	return out;


