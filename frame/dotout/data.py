
from stdio import puts, fputs, fprintf;

from frame.ExpressionTable.Global.self import Global;
from frame.ExpressionTable.Phi.self import Phi;

def dotout_data(all_blocks, expt):
	fstream = open("data.gz", "w");
	fputs("""
digraph mygraph {
	fontname="Helvetica,Arial,sans-serif"
	node [fontname="Helvetica,Arial,sans-serif"]
	edge [fontname="Helvetica,Arial,sans-serif", colorscheme=dark28]
	node [shape=box colorscheme=dark28];
	
	"0" [label="{{<out_vr0> %vr0 | <out_vr1> %vr1 | <out_vr2> %vr2 | <out_vr3> %vr3}}" shape="record"];
	
	""", fstream);
	
	for i, a in enumerate(all_blocks):
		ins = " | ".join(f"<in_{k[1:]}> {k}" for k, v in a.givens.items());
		outs = " | ".join(f"<out_{c[1:]}> {c}" for c in a.changes);
		dot_label = "{{%s} | <label> %s | {%s}}" % (ins, a.label, outs);
		node = f"\t\"{id(a)}\" [label=\"{dot_label}\" shape=\"record\"];\n";
		fputs(node, fstream);
		for reg, v in a.givens.items():
			e = expt.valnum_to_exp(v);
			color = f"[color={int(reg[3:]) % 7 + 1}]";
			if type(e) is Global:
				src = e.version;
				fputs(f"\t\"{src}\":out_{reg[1:]}:s -> \"{id(a)}\":in_{reg[1:]}:n {color};", fstream);
			elif type(e) is Phi:
				if "dotout" not in vars(e):
					fputs(f"\"{id(e)}\" [label=\"𝜙\" shape=\"circle\"] {color};", fstream);
					for v in e.versions:
						fputs(f"\t\"{v}\":out_{reg[1:]}:s -> \"{id(e)}\" {color}", fstream);
					e.dotout = None;
				fputs(f"\"{id(e)}\" -> \"{id(a)}\":in_{reg[1:]}:n {color};", fstream);
			else:
				assert(not "TODO");
	fputs("""
}
	""", fstream);
	
	fstream.close();















