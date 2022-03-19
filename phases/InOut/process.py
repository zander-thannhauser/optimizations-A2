
from debug import *;

from .self import InOutPhase;

#def skim_i2is(block):
#	enter(f"skim_i2is(block.rank = {block.rank})");
#	
#	i2is = [];
#	
#	for inst in block.instructions:
#		operation = inst.operation;
#		if operation == "i2i" and (out := inst.outs[0]) not in i2is:
#			i2is.append(out);
#	
#	block.i2is = i2is;
#	
#	dprint(f"block.i2is = {block.i2is}");
#	
#	exit("return;");

def InOutPhase_process(self, all_blocks, **_):
	enter(f"InOutPhase.process(block.po = {self.block.po})");
	
	block = self.block;
	
	ins = set();
	outs = set();
	
	# union children's needs
	for child in block.children:
		ins.update(child.ins);
	
	todo = [];
	
	if block == all_blocks[0]:
		# I'm the start block
		# so I just magically provide %vr{0,1,2,3}
		
		outs.update(["%vr0", "%vr1", "%vr2", "%vr3"]);
		
		ins.difference_update(outs);
		
		if len(ins):
			assert(not "undefined register used!");
	else:
		# the last instruction might need something too (conditional branch):
		ins.update(i for i in block.instructions[-1].ins if i.startswith("%vr"));
		
		dprint(f"ins = {ins}");
		dprint(f"outs = {outs}");
		
		for inst in block.instructions[-2::-1]:
			dprint(inst);
			if any(o in ins for o in inst.outs) or \
					inst.operation in ["i2i", "iwrite", "store"]:
				if inst.operation == "i2i":
					outs.update(inst.outs);
				ins.difference_update(inst.outs);
				ins.update(i for i in inst.ins if i.startswith("%vr"));
			else:
				inst.useless = True;
	
	dprint(f"ins = {ins}, outs = {outs}");
	
	
	if "in-out" not in block.has_done or block.ins != ins:
		for parent in block.parents:
			todo.append(InOutPhase(parent));
		
		block.ins = ins;
		block.outs = outs;
		block.has_done.add("in-out");
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;















