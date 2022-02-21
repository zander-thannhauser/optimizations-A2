
from stdio import puts, fputs, fprintf;

def dotout_data(all_blocks):
	fstream = open("test.gz", "w");
	fputs("""
digraph mygraph {
	fontname="Helvetica,Arial,sans-serif"
	node [fontname="Helvetica,Arial,sans-serif"]
	edge [fontname="Helvetica,Arial,sans-serif"]
	node [shape=box];
	""", fstream);
	
	for a in all_blocks:
		dot_label = "{{1 | 2 | 3} | <label> %s | {1 | 2 | 3}}" % a.label;
		node = f"\t\"{id(a)}\" [label=\"{dot_label}\" shape=\"record\"];\n";
		fputs(node, fstream);
		for c in a.children:
			fprintf(fstream, "\t\"%s\":label:e -> \"%s\":label:w\n", id(a), id(c));
	
	fputs("""
}
	""", fstream);
	
	fstream.close();


