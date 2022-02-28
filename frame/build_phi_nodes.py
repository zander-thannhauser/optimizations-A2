
from .ExpressionTable.Phi.self import Phi;
from .ExpressionTable.Global.self import Global;

def build_phi_nodes(all_blocks, expt):
	for b in all_blocks:
		newgivens = dict();
		for reg, versions in b.givens.items():
			if len(versions) > 1:
				valnum = expt.exp_to_valnum(Phi(reg, versions));
			else:
				version = list(versions)[0]
				valnum = expt.exp_to_valnum(Global(reg, version));
			newgivens[reg] = valnum;
		b.givens = newgivens;
