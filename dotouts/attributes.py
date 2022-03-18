
from .counter import counter;

from debug import *;

def dotout_attributes(all_blocks, **_):
	
	enter("dotout_attributes()");
	
	stream = open(f"gen/{counter[0]}.txt", "w");
	
	print("""
digraph mygraph {

	node [shape=box];
	
	graph[bgcolor="#444444"];
	
	""", file = stream);
	
	for b in all_blocks:
		bid = id(b);
		
		print(f"""
			\"{bid}\" [{' '.join(f'{k}="{v}"' for k, v in b.attributes.items())}];
		""", file = stream);
		
		for c in b.children:
			print(f"\"{bid}\":s -> \"{id(c)}\":n [style=bold]", file = stream);
		
	print("""
}
	""", file = stream);
	
	stream.close();
	
	counter[0] += 1;
	
	exit("return;");
	


