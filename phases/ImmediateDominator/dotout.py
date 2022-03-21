
from debug import *;

from phases.self import Phase;

from ExpressionTable.self import ExpressionTable;
from ExpressionTable.Phi.self import Phi;
#from ExpressionTable.Global.self import Global;

def ImmediateDominatorPhase_dotout(self, all_blocks, expression_table, **_):
	
	enter("ImmediateDominatorPhase.dotout()");
	
	stream = open(f"gen/{Phase.counter}.txt", "w");
	
	print("""
digraph mygraph {

	node [shape=record];
	
	graph [bgcolor=black];
	
	edge [color=white]
	
	node [fontcolor=black color=white];
	
	""", file = stream);
	
	valnums = set();
	
	for b in all_blocks:
		attributes = b.attributes.copy();
		
		ins = " | ".join(f"<in_{r[1:]}> {r}" for r in b.ins);
		
		label = attributes["label"];
		
		outs = " | ".join(f"<out_{r[1:]}> {r}" for r in b.outs);
		
		attributes["label"] = "{ { " + ins + "} | " + label + " | { " + outs + " } }"
		
		print(f"""
			\"{id(b)}\" [{' '.join(f'{k}="{v}"' for k, v in attributes.items())}];
		""", file = stream);
		
		for c in b.children:
			print(f"\"{id(b)}\":s -> \"{id(c)}\":n [style=bold]", file = stream);
		
		if b.immedate_dominator:
			print(f"""
				"{id(b.immedate_dominator)}":s -> "{id(b)}":n
				[color="#555555" style=bold]
			""", file = stream);
		
		for r, valnum in b.incoming_phis.items():
			hue = valnum / ExpressionTable.valcounter;
			if valnum not in valnums:
				exp = expression_table.vntoex(valnum);
				style = f"shape=circle style=filled color=\"{hue} 1 1\""
				if type(exp) is Phi:
					print(f"""
						\"{valnum}\" [label="𝜙" {style}];
					""", file = stream);
					for src in exp.sources:
						fillcolor = src.attributes["fillcolor"];
						print(f"""
							\"{id(src)}\":\"out_{r[1:]}\":s -> \"{valnum}\"
							 [style=dashed color=\"{fillcolor}\"]
						""", file = stream);
				elif type(exp) is Global:
					rpo = exp.source.rpo
					print(f"""
						\"{valnum}\" [label=<{r}<sub>{rpo}</sub>> {style}];
					""", file = stream);
					fillcolor = exp.source.attributes["fillcolor"];
					print(f"""
						\"{id(exp.source)}\":\"out_{r[1:]}\":s -> \"{valnum}\"
						 [style=dashed color=\"{fillcolor}\"]
					""", file = stream);
				else:
					assert(not "TODO");
				
				valnums.add(valnum);
			print(f"""
				\"{valnum}\" -> \"{id(b)}\":\"in_{r[1:]}\":n
				 [style=dashed color=\"{hue} 1 1\"];
			""", file = stream);
		
	print("""
}
	""", file = stream);
	
	stream.close();
	
	Phase.counter += 1;
	
	exit("return;");
















