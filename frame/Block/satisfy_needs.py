
#from debug import *;

##from .provide import Block_find;

#def Block_satisfy_needs(self, expt):
#	dprint(f"satisfy_needs(self = {self.label})");
#	# for n in self.needs:
#		
#	assert(not "TODO");

##	indent();
##	written_to = set();
##	for inst in self.instructions:
##		# print(written_to);
##		# print(inst.ins);
##		for i in inst.ins:
##			if True \
##				and i[:3] == "%vr" \
##				and i not in written_to \
##				and i not in self.needs:
##				dprint(f"I need {i}");
##				found = Block_find(self, i, expt);
##				if found is None:
##					assert(not "NOPE");
##				self.needs[i] = found;
##		written_to.update(inst.outs);
##	# print(self.needs);
##	unindent();
