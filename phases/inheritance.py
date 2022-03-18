
from debug import *;

def skim_i2is(block):
	enter(f"skim_i2is(block.rank = {block.rank})");
	
	i2is = [];
	
	for inst in block.instructions:
		operation = inst.operation;
		if operation == "i2i" and (out := inst.outs[0]) not in i2is:
			i2is.append(out);
	
	block.i2is = i2is;
	
	dprint(f"block.i2is = {block.i2is}");
	
	exit("return;");

def inheritance_phase(block, **_):
	enter(f"inheritance_phase(block.rank = {block.rank})");
	
	todo = [];
	
	if "i2is" not in vars(block):
		skim_i2is(block);
	
	giving = block.given.copy();
	
	for i2i in block.i2is:
		giving[i2i] = set([block]);
	
	for child in block.children:
		changed = False;
		
		for register, sources in giving.items():
			if register not in child.given:
				changed = True;
				child.given[register] = sources;
			elif any(source not in child.given[register] for source in sources):
				changed = True;
				child.given[register].update(sources);
		
		dprint(f"{block.rank} onto {child.rank}: changed = {changed}");
		
		if changed:
			todo.append((2, child));
	
	exit(f"return {[(p, str(b)) for p, b in todo]}");
	return todo;














