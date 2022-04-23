
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
	outs = list();
	
	# union children's needs
	for child in block.children:
		ins.update(child.ins);
	
	todo = [];
	
	if block == all_blocks[0]:
		# I'm the start block
		# so I just magically provide %vr{0,1,2,3} + args
		
		outs = block.magic_provides;
		
		ins.difference_update(outs);
		
		if len(ins):
			assert(not "undefined register used!");
	else:
		# the last instruction might need something too (conditional branch):
		
		if block.jump:
			ins.update(i for i in block.jump.ins if i.startswith("%vr"));
		
		dprint(f"ins = {ins}");
		dprint(f"outs = {outs}");
		
		new_instructions = [];
		
		for inst in block.instructions[::-1]:
			dprint(f"inst = {inst}");
			# dprint(f"inst.out = {inst.out}");
			
			if (inst.out in ins) or inst.op in \
					["i2i", "iwrite", "iread", "store", "ret", "swrite", "call", "putchar"]:
				# either it's useful or protected:
				if inst.op == "i2i" and inst.out not in outs:
					outs.insert(0, inst.out);
				ins.discard(inst.out);
				if inst.op != "loadI":
					print(f"inst.ins = {inst.ins}");
					ins.update(inst.ins);
					# ins.update(i for i in inst.ins if i.startswith("%vr"));
					# assert(not "CHECK");
				new_instructions.insert(0, inst);
			elif inst.op in ["loadI", "load"]:
				dprint("USELESS!");
			else:
				assert(not "TODO");
		
		block.instructions = new_instructions;
	
	dprint(f"ins = {ins}, outs = {outs}");
	 #assert(not "CHECK");
	
	if "in-out" not in block.has_done or block.ins != ins:
		for parent in block.parents:
			todo.append(InOutPhase(parent));
		
		block.ins = ins;
		block.outs = outs;
		block.has_done.add("in-out");
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;















