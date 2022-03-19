
from debug import *;

from phases.self import Phase;

from ExpressionTable.self import ExpressionTable;
from ExpressionTable.Phi.self import Phi;
from ExpressionTable.Global.self import Global;

def OptimizePhase_dotout(self, all_blocks, expression_table, **_):
	
	enter("OptimizePhase.dotout()");
	
	stream = open(f"gen/{Phase.counter}.txt", "w");
	
	print("""
digraph mygraph {

	node [shape=record];
	
	graph [bgcolor=black];
	
	edge [color=white]
	
	node [fontcolor=white color=white];
	
	""", file = stream);
	
	valnums = set();
	
	for block in all_blocks:
#	for block in [all_blocks[1]]:
		
		bid = id(block);
		
		for valnum in block.given_valnums.values():
			if valnum not in valnums:
				exp = expression_table.vntoex(valnum);
				
				hue = valnum / ExpressionTable.valcounter;
				
				print(f"""
					\"{valnum}\" [shape=doublecircle color=\"{hue} 1 1\"];
				""", file = stream);
				
				valnums.add(valnum);
		
		if "optimized" in block.has_done:
			inst_keys = [];
			
			for inst in block.instructions:
				me = inst.dotout(stream);
				inst_keys.append(me);
			
			for index, key in enumerate(inst_keys):
				if index:
					print(f"\"{inst_keys[index-1]}\":s -> \"{key}\":n;", file = stream);
		else:
			for index, inst in enumerate(block.instructions):
				ins = " | ".join(inst.ins);
				
				label = "{{" + inst.op + " | " + ins
				
				if inst.out:
					label += " | ⟶ | " + inst.out
				
				label += "}}";
				
				print(f"\"{bid}_{index}\" [label=\"{label}\"];", file = stream);
				
				if index:
					print(f"\"{bid}_{index-1}\" -> \"{bid}_{index}\";", file = stream);
		
	print("""
}
	""", file = stream);
	
	stream.close();
	
	Phase.counter += 1;
	
	exit("return;");
















