
from debug import *;

from .self import PhiPhase;

from ExpressionTable.Phi.self import Phi;
#from ExpressionTable.Global.self import Global;

def PhiPhase_process(self, expression_table, **_):
	enter(f"PhiPhase.process(self.block.rpo = {self.block.rpo})");
	
	block = self.block;
	
	block.attributes["fillcolor"] = f"{block.hue} 1 0.5";
	
	for register, sources in block.given.items():
		dprint(f"register = {register}, sources = {[str(s) for s in sources]}");
		if not len(sources):
			fprintf(stderr, "use of undefined register!");
			sys.exit(1);
		elif len(sources) > 1:
			exp = Phi(register, sources);
			result = expression_table.extovn(exp);
			block.incoming_phis[register] = result.valnum;
			if result.is_new:
				for source in sources:
					source.outgoing_phis[register] = result.valnum;
			
	todo = [];
	
	for child in block.children:
		if "phis" not in child.has_done:
			todo.append(PhiPhase(child));
			child.has_done.add("phis");
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;














