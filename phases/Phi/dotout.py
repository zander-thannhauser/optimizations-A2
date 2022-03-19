
from debug import *;

from phases.self import Phase;

from ExpressionTable.Phi.self import Phi;
from ExpressionTable.Global.self import Global;

def PhiPhase_dotout(self, all_blocks, expression_table, **_):
	
	enter("PhiPhase.dotout()");
	
	stream = open(f"gen/{Phase.counter}.txt", "w");
	
	print("""
digraph mygraph {

	node [shape=record];
	
	graph[bgcolor="#444444"];
	
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
		
		if (b.given_valnums):
			for r, valnum in b.given_valnums.items():
				if valnum not in valnums:
					exp = expression_table.vntoex(valnum);
					style = "shape=circle style=filled color=white"
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
					 [style=dashed color=white]
				""", file = stream);
		else:
			for r, ps in b.given.items():
				for p in ps:
					fillcolor = p.attributes["fillcolor"];
					print(f"""
						\"{id(p)}\":\"out_{r[1:]}\":s -> \"{id(b)}\":\"in_{r[1:]}\":n
						 [style=dashed color=\"{fillcolor}\"]
					""", file = stream);
		
	print("""
}
	""", file = stream);
	
	stream.close();
	
	Phase.counter += 1;
	
	exit("return;");
















