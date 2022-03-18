
from debug import *;

from ExpressionTable.Phi.self import Phi;

from ExpressionTable.Global.self import Global;

def phi_phase(block, expression_table, **_):
	
	enter(f"phi_phase(block.rank = {block.rank})");
	
	for register, sources in block.given.items():
		dprint(f"register = {register}, sources = {[str(s) for s in sources]}");
		if len(sources) > 1:
			exp = Phi(register, sources);
		else:
			exp = Global(register, *sources);
		valnum = expression_table.exp_to_valnum(exp);
		block.given_valnums[register] = valnum;
	
	todo = [];
	
	for child in block.children:
		if "phis" not in child.has_done:
			todo.append((3, child));
			child.has_done.add("phis");
	
	exit(f"return {[(p, str(b)) for p, b, *_ in todo]}");
	return todo;


