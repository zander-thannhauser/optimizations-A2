
from debug import *;

from ExpressionTable.self import ExpressionTable;
from ExpressionTable.Constant.self import Constant;

def Instruction_dotout(self, stream):
	enter("Instruction.dotout()");
	
	dprint(f"self.op = {self.op}");
	dprint(f"self.ins = {self.ins}");
	dprint(f"self.out = {self.out}");
	
	me = self.out if self.out else id(self);
	
	if type(self.out) is int:
		color = f"{self.out / ExpressionTable.valcounter} 1 1";
	else:
		color = "white";
	
	def connect_param(src, port, stream):
		color = f"{src / ExpressionTable.valcounter} 1 1";
		print(f"""
			"{src}":s -> "{me}":{port}:n [color="{color}"];
		""", file = stream);
	
	match self.op:
		case "loadI":
			literal,  = self.ins;
			ins = f"<1> {literal.value}"
		
		case "addI":
			value, const = self.ins;
			connect_param(value, f"1", stream);
			ins = f"<1> {value} | <2> {const}";
		
		case "storeAI":
			value, dest, offset = self.ins;
			connect_param(value, f"1", stream);
			connect_param(dest,  f"2", stream);
			ins = f"<1> {value} | <2> {dest} | <3> {offset}";
		
		case "loadAI":
			base, offset = self.ins;
			connect_param(base, f"1", stream);
			ins = f"<1> {base} | <2> {offset}";
		
		case "comp":
			left, right = self.ins;
			connect_param(left, f"1", stream);
			connect_param(right, f"2", stream);
			ins = f"<1> {left} | <2> {right}";
		
		case "not":
			inner,  = self.ins;
			connect_param(inner, f"1", stream);
			ins = f"<1> {inner}";
		
		case "cbrne":
			inner,  = self.ins;
			connect_param(inner, f"1", stream);
			ins = f"<1> {inner}";
		
		case _:
			dprint(f"self.op == {self.op}");
			assert(not "TODO");
	
	label = "{{" + self.op + " | " + ins + "}}";
	
	print(f"""
		"{me}" [shape=record label="{label}" color="{color}"];
	""", file = stream);
	
	exit(f"return {me};");
	return me;














