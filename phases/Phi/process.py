
from debug import *;

from .self import PhiPhase;

from ExpressionTable.Phi.self import Phi;
from ExpressionTable.Global.self import Global;

def PhiPhase_process(self, expression_table, **_):
	enter(f"PhiPhase.process(self.block.rpo = {self.block.rpo})");
	
	block = self.block;
	
	for register, sources in block.given.items():
		dprint(f"register = {register}, sources = {[str(s) for s in sources]}");
		if len(sources) > 1:
			exp = Phi(register, sources);
		else:
			exp = Global(register, *sources);
		result = expression_table.extovn(exp);
		block.given_valnums[register] = result.valnum;
	
	todo = [];
	
	for child in block.children:
		if "phis" not in child.has_done:
			todo.append(PhiPhase(child));
			child.has_done.add("phis");
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;














