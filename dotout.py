
from stdio import puts, fputs, fprintf;

counter = 0;

def dotout(all_blocks):
	
	global counter;
	
	fstream = open(f"gen/{counter}.txt", "w");
	
	fputs("""
digraph mygraph {
	fontname="Helvetica,Arial,sans-serif"
	node [fontname="Helvetica,Arial,sans-serif"]
	edge [fontname="Helvetica,Arial,sans-serif"]
	node [shape=box];
	""", fstream);
	
	labels = set();
	read_order = set();
	
	n = len(all_blocks);
	
	for b in all_blocks:
		bid = id(b);
		
		instructions = " | " .join(i.operation for i in b.instructions);
		
		attributes = {
			"label": "{" + instructions + "}",
			"shape": "record",
			"style": "filled",
			"fillcolor": f"{max(0, b.rank / (n + 1))} 1 1",
		};
		
		print(bid, file = fstream);
		print('[', \
			' '.join(f'{k}="{v}"' for k, v in attributes.items()), \
		']', file = fstream);
		
		for c in b.children:
			print(f"\t\"{bid}\":s -> \"{id(c)}\":n", file = fstream);
		
	fputs("""
}
	""", fstream);
	
	fstream.close();
	
	counter += 1;


















