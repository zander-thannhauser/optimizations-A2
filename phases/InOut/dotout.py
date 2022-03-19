
from debug import *;

from phases.self import Phase;

def InOutPhase_dotout(self, all_blocks, **_):
	
	enter("InOutPhase.dotout()");
	
	stream = open(f"gen/{Phase.counter}.txt", "w");
	
	print("""
digraph mygraph {

	node [shape=record];
	
	graph[bgcolor="#444444"];
	
	""", file = stream);
	
	for b in all_blocks:
		bid = id(b);
		
		attributes = b.attributes.copy();
		
		ins = " | ".join(f"<{r[1:]}> {r}" for r in b.ins);
		
		label = attributes["label"];
		
		outs = " | ".join(f"<{r[1:]}> {r}" for r in b.outs);
		
		attributes["label"] = "{ { " + ins + "} | " + label + " | { " + outs + " } }"
		
		print(f"""
			\"{id(b)}\" [{' '.join(f'{k}="{v}"' for k, v in attributes.items())}];
		""", file = stream);
		
		for c in b.children:
			print(f"\"{bid}\":s -> \"{id(c)}\":n [style=bold]", file = stream);
		
	print("""
}
	""", file = stream);
	
	stream.close();
	
	Phase.counter += 1;
	
	exit("return;");

