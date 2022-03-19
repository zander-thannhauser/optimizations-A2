
from stdio import printf, puts;

from Block.self import Block;

from Instruction.self import Instruction;

from debug import *;

def read_block(t):
	label = ""
	
	if (t.token[0] == '.'):
		label = t.token;
		# printf("label == \"%s\"\n", label);
		assert(next(t) == ":");
		t.next();
	
	instructions = [];
	
	children = ["(fallthrough)"]; # indicates we also want fallthrough
	
	while t.token and (t.token[0] != '.'):
		ins = []
		out = None
		operation = t.token;
		# printf("operation == \"%s\"\n", operation);
		t.next();
		
		if operation not in ["ret", "nop", "jumpI"]:
			ins.append(t.token);
			t.next();
			while t.token == ',':
				t.next();
				ins.append(t.token);
				t.next();
		
		if operation not in \
				["ret", "nop", "iwrite", "fwrite", "swrite", "iread", "iret", "call"]:
			# printf("t.token == \"%s\"\n", t.token);
			assert(t.token in ["->", "=>"]);
			t.next();
			out = t.token;
			t.next();
		
		if operation in ["store", "storeAI", "storeAO"]:
			ins.append(out); out = None;
		
		if operation == "ret":
			operation = "jumpI";
			out = "(return)";
		
		# print(operation, ins, outs);
		
		instructions.append(Instruction(operation, ins, out));
		
		if operation == "jumpI":
			assert(out);
			children = [out];
		elif operation == "jump":
			assert(not "NOPE");
		elif operation in ["cbr", "cbrne", \
				"cbr_LT", "cbr_LE", "cbr_GT", "cbr_GE", "cbr_EQ", "cbr_NE"]:
			dprint(f"out == {out}");
			assert(out);
			children.append(out);
			break;
	
	return Block(label, instructions, children);
















