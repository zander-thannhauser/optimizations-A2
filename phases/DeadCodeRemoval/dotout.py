
from debug import *;

from phases.self import Phase;

from ExpressionTable.self import ExpressionTable;

def DeadCodeRemoval_dotout(self, all_blocks, expression_table, **_):
	
	enter("DeadCodeRemoval.dotout()");
	
	stream = open(f"gen/{Phase.counter}.txt", "w");
	
	print("""
digraph mygraph {

	node [shape=record];
	
	graph [bgcolor=black];
	
	edge [color=white]
	
	node [fontcolor=white color=white];
	
	""", file = stream);
	
	valnums = set();
	
	all_instruction_ids = {};
	
	for block in all_blocks:
		
		bid = id(block);
		
		for valnum in block.incoming_phis.values():
			if valnum not in valnums:
				exp = expression_table.vntoex(valnum);
				
				hue = valnum / ExpressionTable.valcounter;
				
				print(f"""
					\"{valnum}\" [shape=doublecircle color=\"{hue} 1 1\"];
				""", file = stream);
				
				valnums.add(valnum);
		
		inst_keys = [];
		
		instructions = block.instructions.copy();
		
		if block.jump is not None:
			instructions.append(block.jump);
		
		if len(instructions) == 0:
			key = f"{bid}_empty";
			print(f"""
				\"{key}\" [label="(empty)" color=white];
			""", file = stream);
			inst_keys = [key];
		else:
			for inst in instructions:
				me = inst.dotout(stream);
				inst_keys.append(me);
		
		all_instruction_ids[block.rpo] = inst_keys;
	
	for block in all_blocks:
		
		ids = all_instruction_ids[block.rpo];
		
		n = len(ids) - 1;
		
		for index, key in enumerate(ids):
			if index < n:
				print(f"\"{key}\":s -> \"{ids[index+1]}\":n;", file = stream);
			else:
				directions = [[""], ["s"], ["w", "e"]][len(block.children)];
				for d, child in zip(directions, block.children):
					first_id = all_instruction_ids[child.rpo][0];
					print(f"\"{key}\":{d} -> \"{first_id}\":n;", file = stream);
			
	print("""
}
	""", file = stream);
	
	stream.close();
	
	dprint(f"Phase.counter = {Phase.counter}");
	
	Phase.counter += 1;
	
	exit("return;");























