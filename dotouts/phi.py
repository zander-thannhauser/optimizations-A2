
from .counter import counter;

from debug import *;

from ExpressionTable.Phi.self import Phi;
from ExpressionTable.Global.self import Global;

def dotout_phi(all_blocks, expression_table, **_):
	
	enter("dotout_phi()");
	
	dprint(f"counter = {counter[0]}");
	
	stream = open(f"gen/{counter[0]}.txt", "w");
	
	print("""
digraph mygraph {
	
	node [shape=record];
	
	graph[bgcolor="#444444"];
	
	""", file = stream);
	
	valnums = set();
	
	for b in all_blocks:
		
		attributes = b.attributes.copy();
		
		ins = " | ".join(f"<{r[1:]}> {r}" for r in b.given.keys());
		
		label = attributes["label"];
		
		attributes["label"] = "{ { " + ins + "} | " + label + " }"
		
		print(f"""
			\"{id(b)}\" [{' '.join(f'{k}="{v}"' for k, v in attributes.items())}];
		""", file = stream);
		
		if (b.given_valnums):
			for register, valnum in b.given_valnums.items():
				if valnum not in valnums:
					exp = expression_table.valnum_to_exp(valnum);
					style = "shape=circle style=filled color=white"
					if type(exp) is Phi:
						print(f"""
							\"{valnum}\" [label="𝜙" {style}];
						""", file = stream);
						for src in exp.sources:
							fillcolor = src.attributes["fillcolor"];
							print(f"""
								\"{id(src)}\":s -> \"{valnum}\"
								 [style=dashed color=\"{fillcolor}\"]
							""", file = stream);
					elif type(exp) is Global:
						rank = exp.source.rank
						print(f"""
							\"{valnum}\" [label=<{register}<sub>{rank}</sub>> {style}];
						""", file = stream);
						fillcolor = exp.source.attributes["fillcolor"];
						print(f"""
							\"{id(exp.source)}\":s -> \"{valnum}\"
							 [style=dashed color=\"{fillcolor}\"]
						""", file = stream);
					else:
						assert(not "TODO");
					
					valnums.add(valnum);
				print(f"""
					\"{valnum}\" -> \"{id(b)}\":\"{register[1:]}\":n
					 [style=dashed color=white]
				""", file = stream);
		else:
			for r, ps in b.given.items():
				for p in ps:
					fillcolor = p.attributes["fillcolor"];
					print(f"""
						\"{id(p)}\":s -> \"{id(b)}\":\"{r[1:]}\":n
						 [style=dashed color=\"{fillcolor}\"]
					""", file = stream);
		
		for c in b.children:
			print(f"\"{id(b)}\":s -> \"{id(c)}\":n [style=bold]", file = stream);
		
	print("""
}
	""", file = stream);
	
	stream.close();
	
	counter[0] += 1;
	
	exit("return;");






