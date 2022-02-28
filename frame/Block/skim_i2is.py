
def Block_skim_i2is(self):
	for inst in self.instructions:
		operation = inst.operation;
		if operation == "i2i" and (out := inst.outs[0]) not in self.changes:
			self.changes.append(out);
	print(self.changes);


