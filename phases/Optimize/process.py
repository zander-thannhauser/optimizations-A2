
from debug import *;

from .self import OptimizePhase;

def OptimizePhase_process(self, all_blocks, **_):
	enter(f"OptimizePhase.process(self.block.rpo = {self.block.rpo})");
	
	todo = [];
	block = self.block;
	
	# write more code here!
	
#	for child in block.children:
#		if "optimize" not in child.has_done:
#			todo.append(OptimizePhase(child));
#			child.has_done.add("optimize");
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;



















