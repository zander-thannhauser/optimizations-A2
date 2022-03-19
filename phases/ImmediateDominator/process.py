
from debug import *;

from .self import ImmediateDominatorPhase;

from ExpressionTable.Phi.self import Phi;
from ExpressionTable.Global.self import Global;

def intersect(i, j):
	finger1 = i
	finger2 = j
	while finger1 != finger2:
		while (finger1).rpo > (finger2).rpo: finger1 = finger1.immedate_dominator;
		while (finger2).rpo > (finger1).rpo: finger2 = finger2.immedate_dominator;
	return finger1;

def ImmediateDominatorPhase_process(self, all_blocks, **_):
	enter(f"ImmediateDominatorPhase.process(self.block.rpo = {self.block.rpo})");
	
	todo = [];
	block = self.block;
	
	if block == all_blocks[0]:
		new_idom = block;
	else:
		processed_predessors = [p for p in block.parents if p.immedate_dominator];
		new_idom = processed_predessors[0];
		
		for p in processed_predessors[1:]:
			new_idom = intersect(p, new_idom);
		
	if block.immedate_dominator != new_idom:
		block.immedate_dominator = new_idom;
		for child in block.children:
			todo.append(ImmediateDominatorPhase(child));
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;



















