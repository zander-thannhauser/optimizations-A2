
def Instruction_str(self):
	out = self.op + " " + ', '.join(str(s) for s in self.ins);
	if self.out:
		out += " => " + str(self.out);
	return out;


