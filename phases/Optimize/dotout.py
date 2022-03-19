
from debug import *;

from phases.self import Phase;

from ExpressionTable.Phi.self import Phi;
from ExpressionTable.Global.self import Global;

def OptimizePhase_dotout(self, all_blocks, expression_table, **_):
	
	enter("OptimizePhase.dotout()");
	
	stream = open(f"gen/{Phase.counter}.txt", "w");
	
	print("""
digraph mygraph {

	node [shape=record];
	
	graph[bgcolor="#444444"];
	
	""", file = stream);
	
	valnums = set();
	
	for b in all_blocks:
		
		bid = id(b);
		
		print(f""" subgraph "cluster_{id(b)}" """ + """ {
			
		""", file = stream);
		
		fillcolor = b.attributes["fillcolor"];
		
		print(f"graph [bgcolor=\"{fillcolor}\"];", file = stream);
		
		for r in b.ins:
			print(f"\"{bid}_in_{r}\" [label=\"{r}\" shape=invtriangle];", file = stream);
		
		for r in b.outs:
			print(f"\"{bid}_out_{r}\" [label=\"{r}\" shape=invtriangle];", file = stream);
		
		print(f"\"{bid}_instruction\" [label=\"instructions\" shape=box];", file = stream);
		
		for r in b.ins:
			print(f"\"{bid}_in_{r}\":s -> \"{bid}_instruction\":n;", file = stream);
		
		for r in b.outs:
			print(f"\"{bid}_instruction\":s -> \"{bid}_out_{r}\":n;", file = stream);
		
		print("}", file = stream);
		
#		for r, valnum in b.given_valnums.items():
#			if valnum not in valnums:
#				exp = expression_table.valnum_to_exp(valnum);
#				style = "shape=circle style=filled color=white"
#				if type(exp) is Phi:
#					print(f"""
#						\"{valnum}\" [label="𝜙" {style}];
#					""", file = stream);
#					for src in exp.sources:
#						fillcolor = src.attributes["fillcolor"];
#						print(f"""
#							\"{id(src)}\":\"out_{r[1:]}\":s -> \"{valnum}\"
#							 [style=dashed color=\"{fillcolor}\"]
#						""", file = stream);
#				elif type(exp) is Global:
#					rpo = exp.source.rpo
#					print(f"""
#						\"{valnum}\" [label=<{r}<sub>{rpo}</sub>> {style}];
#					""", file = stream);
#					fillcolor = exp.source.attributes["fillcolor"];
#					print(f"""
#						\"{id(exp.source)}\":\"out_{r[1:]}\":s -> \"{valnum}\"
#						 [style=dashed color=\"{fillcolor}\"]
#					""", file = stream);
#				else:
#					assert(not "TODO");
#				
#				valnums.add(valnum);
#			print(f"""
#				\"{valnum}\" -> \"{id(b)}\":\"in_{r[1:]}\":n
#				 [style=dashed color=white]
#			""", file = stream);
		
	print("""
}
	""", file = stream);
	
	stream.close();
	
	Phase.counter += 1;
	
	exit("return;");
















