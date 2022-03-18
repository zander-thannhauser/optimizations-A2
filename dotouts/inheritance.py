
from stdio import puts, fputs, fprintf;

from .counter import counter;

from debug import *;

def dotout_inheritance(all_blocks, **_):
	
	enter("dotout_inheritance()");
	
	dprint(f"counter = {counter[0]}");
	
	stream = open(f"gen/{counter[0]}.txt", "w");
	
	print("""
digraph mygraph {
	
	node [shape=record];
	
	graph[bgcolor="#444444"];
	
	""", file = stream);
	
	for b in all_blocks:
		
		attributes = b.attributes.copy();
		
		ins = " | ".join(f"<{r[1:]}> {r}" for r in b.given.keys());
		
		label = attributes["label"];
		
		attributes["label"] = "{ { " + ins + "} | " + label + " }"
		
		print(f"""
			\"{id(b)}\" [{' '.join(f'{k}="{v}"' for k, v in attributes.items())}];
		""", file = stream);
		
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


















