
def Instruction_str(self):
	out = self.op + " " + ', '.join(self.ins);
	if self.out:
		out += " => " + self.out;
	return out;


