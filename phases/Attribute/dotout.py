
from debug import *;

from phases.self import Phase;

def AttributePhase_dotout(self, all_blocks, **_):
	
	enter("AttributePhase.dotout()");
	
	stream = open(f"gen/{Phase.counter}.txt", "w");
	
	dprint(f"Phase.counter = {Phase.counter}");
	
	print("""
digraph mygraph {

	node [shape=box];
	
	graph [bgcolor=black];
	
	edge [color=white]
	
	node [fontcolor=black color=white];
	
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
	
	Phase.counter += 1;
	
	exit("return;");


