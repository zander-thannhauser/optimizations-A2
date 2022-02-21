
from stdio import puts, fputs, fprintf;

def dotout_control(all_blocks):
	fstream = open("control.gz", "w");
	fputs("""
digraph mygraph {
	fontname="Helvetica,Arial,sans-serif"
	node [fontname="Helvetica,Arial,sans-serif"]
	edge [fontname="Helvetica,Arial,sans-serif"]
	node [shape=box];
	""", fstream);
	
	for a in all_blocks:
		node = f"\t\"{id(a)}\" [label=\"{a.label}\" shape=circle];\n";
		fputs(node, fstream);
		for c in a.children:
			fprintf(fstream, "\t\"%s\":s -> \"%s\":n\n", id(a), id(c));
	
	fputs("""
}
	""", fstream);
	
	fstream.close();

