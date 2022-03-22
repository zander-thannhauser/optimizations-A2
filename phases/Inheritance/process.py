
from debug import *;

from .self import InheritancePhase;

def InheritancePhase_process(self, **_):
	enter(f"InheritancePhase.process(self.block.rpo = {self.block.rpo})");
	
	todo = [];
	
	block = self.block;
	
	giving = block.given.copy();
	
	for out in block.outs:
		giving[out] = set([block]);
	
	for child in block.children:
		changed = False;
		
		for register in child.ins:
			assert(register in giving);
			
			sources = giving[register];
			
			if register not in child.given:
				changed = True;
				child.given[register] = sources;
			elif any(source not in child.given[register] for source in sources):
				changed = True;
				child.given[register].update(sources);
		
		dprint(f"{block.rpo} onto {child.rpo}: changed = {changed}");
		
		if changed or "inheritance" not in child.has_done:
			todo.append(InheritancePhase(child));
			child.has_done.add("inheritance");
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;














