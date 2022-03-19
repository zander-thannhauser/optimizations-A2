
from stdio import printf, puts;

from Block.self import Block;

from Instruction.self import Instruction;

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
		outs = []
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
			outs.append(t.token);
			t.next();
			while t.token == ',':
				t.next();
				outs.append(t.token);
				t.next();
		
		if operation in ["store", "storeAI", "storeAO"]:
			ins += outs; outs = [];
		
		if operation == "ret":
			operation = "jumpI";
			outs = ["(return)"];
		
		# print(operation, ins, outs);
		
		instructions.append(Instruction(operation, ins, outs));
		
		if operation == "jumpI":
			children = [outs[0]];
		elif operation == "jump":
			assert(not "NOPE");
		elif operation in ["cbr", "cbrne", \
				"cbr_LT", "cbr_LE", "cbr_GT", "cbr_GE", "cbr_EQ", "cbr_NE"]:
			children.append(outs[0]);
			break;
	
	return Block(label, instructions, children);















