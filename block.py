
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
	jump = None;
	children = ["(fallthrough)"]; # indicates we also want fallthrough
	
	while t.token and (t.token[0] != '.'):
		operation = t.token; ins = []; out = None;
		
		printf("operation == \"%s\"\n", operation);
		t.next();
		
		match (operation):
			
			# those who take one in and zero out:
			case "iwrite" | "swrite":
				ins.append(t.token); t.next();
				instructions.append(Instruction(operation, ins, out));
			
			# those who take one in and one out:
			case "loadI" | "i2i" | "load" \
					| "testeq" | "testne" \
					| "testgt" \
					| "testne" \
					| "testlt" | "testle" :
				ins.append(t.token); t.next();
				assert(t.token == "=>"); t.next();
				out = t.token; t.next();
				instructions.append(Instruction(operation, ins, out));
			
			# those who take two in and one out:
			case "add" | "sub" | "mult" | "comp":
				ins.append(t.token); t.next();
				assert(t.token == ","); t.next();
				ins.append(t.token); t.next();
				assert(t.token == "=>"); t.next();
				out = t.token; t.next();
				instructions.append(Instruction(operation, ins, out));
			
			# store:
			case "store":
				ins.append(t.token); t.next();
				assert(t.token == "=>"); t.next();
				ins.append(t.token); t.next();
				instructions.append(Instruction(operation, ins, out));
			
			# nop:
			case "nop": pass;
			
			# branching:
			case "cbr" | "cbrne":
				ins.append(t.token); t.next();
				assert(t.token == "->"); t.next();
				branch_label = t.token; t.next();
				jump = Instruction(operation, ins, out, branch_label);
				children.append(branch_label);
				break;
			
			case "ret":
				# jump = Instruction("jumpI", ["(return)"], out);
				children = ["(return)"];
				break;
			
			case _:
				assert(not "TODO");
		
	return Block(label, instructions, children, jump);
















