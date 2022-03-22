
from debug import *;

from phases.self import Phase;

def InheritancePhase_dotout(self, all_blocks, **_):
	
	enter("InheritancePhase.dotout()");
	
	stream = open(f"gen/{Phase.counter}.txt", "w");
	
	print("""
digraph mygraph {

	node [shape=record];
	
	graph [bgcolor=black];
	
	edge [color=white]
	
	node [fontcolor=black color=white];
	
	""", file = stream);
	
	for b in all_blocks:
		if b.is_reachable:
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
















