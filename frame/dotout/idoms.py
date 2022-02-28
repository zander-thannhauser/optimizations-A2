
from stdio import fputs, fprintf;

def dotout_idoms(all_blocks):
	fstream = open("idoms.gz", "w");
	fputs("""
digraph mygraph {
	fontname="Helvetica,Arial,sans-serif"
	node [fontname="Helvetica,Arial,sans-serif"]
	edge [fontname="Helvetica,Arial,sans-serif"]
	node [shape=box];
	""", fstream);
	
	for i, b in enumerate(all_blocks):
		node = f"\t\"{id(b)}\" [label=\"{b.label}\" shape=circle];\n";
		fputs(node, fstream);
		fprintf(fstream, "\t\"%s\":s -> \"%s\":n\n", id(b), id(b.immedate_dominator));
	
	fputs("""
}
	""", fstream);
	
	fstream.close();


