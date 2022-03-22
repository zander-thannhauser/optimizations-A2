
from debug import *;

from ExpressionTable.self import ExpressionTable;
from ExpressionTable.Constant.self import Constant;

def Instruction_dotout(self, stream):
	enter("Instruction.dotout()");
	
#	dprint(f"self.op = {self.op}");
#	dprint(f"self.ins = {self.ins}");
#	dprint(f"self.out = {self.out}");
	
	if type(self.out) is int:
		me = self.out;
		color = f"{self.out / ExpressionTable.valcounter} 1 1";
	else:
		me = id(self);
		color = "white";
	
	def connect_param(src, port, stream):
		color = f"{src / ExpressionTable.valcounter} 1 1";
		print(f"""
			"{src}":s -> "{me}":{port}:n [color="{color}"];
		""", file = stream);
	
	match self.op:
		case "add":
			left, right = self.ins;
			connect_param(left, f"1", stream);
			connect_param(right, f"2", stream);
			ins = f"<1> {left} | <2> {right}";
		
		case "addI":
			value, const = self.ins;
			connect_param(value, f"1", stream);
			ins = f"<1> {value} | <2> {const}";
		
		case "cbr":
			inner,  = self.ins;
			connect_param(inner, f"1", stream);
			ins = f"<1> {inner}";
		
		case "cbr_GT" | "cbr_NE" | "cbr_GE" | "cbr_EQ" | "cbr_LE" \
				| "cmp_GT" | "cmp_LT" | "cmp_EQ" | "cmp_NE" | "cmp_LE":
			left, right = self.ins;
			connect_param(left, f"1", stream);
			connect_param(right, f"2", stream);
			ins = f"<1> {left} | <2> {right}";
		
		case "cbrne":
			inner,  = self.ins;
			connect_param(inner, f"1", stream);
			ins = f"<1> {inner}";
		
		case "comp":
			left, right = self.ins;
			connect_param(left, f"1", stream);
			connect_param(right, f"2", stream);
			ins = f"<1> {left} | <2> {right}";
		
		case "i2i":
			inner,  = self.ins;
			me = id(self);
			connect_param(inner, f"1", stream);
			ins = f"<1> {inner}";
			phi_num = self.out;
			color = f"{phi_num / ExpressionTable.valcounter} 1 1";
			print(f"""
				"{me}":s -> "{phi_num}" [color="{color}"];
			""", file = stream);
		
		case "iwrite":
			inner,  = self.ins;
			connect_param(inner, f"1", stream);
			ins = f"<1> {inner}";
		
		case "jumpI":
			inner,  = self.ins;
			ins = f"<1> {inner}";
		
		case "loadAI":
			base, offset = self.ins;
			connect_param(base, f"1", stream);
			ins = f"<1> {base} | <2> {offset}";
		
		case "loadAO":
			left, right = self.ins;
			connect_param(left, f"1", stream);
			connect_param(right, f"2", stream);
			ins = f"<1> {left} | <2> {right}";
		
		case "loadI":
			literal,  = self.ins;
			match literal:
				case Constant():
					ins = f"<1> {literal.value}"
				case str():
					ins = f"<1> \"{literal}\""
				case _:
					assert(not "TODO");
		
		case "ret":
			ins = ""
		
		case "mult":
			assert(not "TODO");
		
		case "multI":
			value, const = self.ins;
			connect_param(value, f"1", stream);
			ins = f"<1> {value} | <2> {const}";
		
		case "not":
			inner,  = self.ins;
			connect_param(inner, f"1", stream);
			ins = f"<1> {inner}";
		
		case "storeAI":
			value, dest, offset = self.ins;
			connect_param(value, f"1", stream);
			connect_param(dest,  f"2", stream);
			ins = f"<1> {value} | <2> {dest} | <3> {offset}";
		
		case "storeAO":
			value, dest, offset = self.ins;
			connect_param(value, f"1", stream);
			connect_param(dest,  f"2", stream);
			connect_param(offset,  f"3", stream);
			ins = f"<1> {value} | <2> {dest} | <3> {offset}";
		
		case "sub":
			left, right = self.ins;
			connect_param(left, f"1", stream);
			connect_param(right, f"2", stream);
			ins = f"<1> {left} | <2> {right}";
		
		case "swrite":
			inner,  = self.ins;
			connect_param(inner, f"1", stream);
			ins = f"<1> {inner}";
		
		case _:
			dprint(f"self.op == {self.op}");
			assert(not "TODO");
	
	label = "{{" + self.op + " | " + ins + "}}";
	
	print(f"""
		"{me}" [shape=record label="{label}" color="{color}"]
		[{"style=filled fontcolor=black" if self.is_critical else ""}];
	""", file = stream);
	
	exit(f"return {me};");
	return me;






















