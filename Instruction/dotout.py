
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
			ins = f"<1> %vr{left} | <2> %vr{right}";
		
		case "addI":
			value, const = self.ins;
			connect_param(value, f"1", stream);
			ins = f"<1> %vr{value} | <2> {const}";
		
		case "cbr":
			inner,  = self.ins;
			connect_param(inner, f"1", stream);
			ins = f"<1> %vr{inner}";
		
		case  "cbr_GT" | "cbr_NE" | "cbr_LT" | "cbr_GE" | "cbr_EQ" | "cbr_LE" \
			| "cmp_GT" | "cmp_NE" | "cmp_LT" | "cmp_GE" | "cmp_EQ" | "cmp_LE":
			left, right = self.ins;
			connect_param(left, f"1", stream);
			connect_param(right, f"2", stream);
			ins = f"<1> %vr{left} | <2> %vr{right}";
		
		case "cbrne":
			inner,  = self.ins;
			connect_param(inner, f"1", stream);
			ins = f"<1> %vr{inner}";
		
		case "call":
			ins = f"{self.label}";
			for i, param in enumerate(self.ins):
				port = f"{i + 1}"
				connect_param(param, port, stream);
				ins += f" | <{port}> %vr{param}";
		
		case "comp":
			left, right = self.ins;
			connect_param(left, f"1", stream);
			connect_param(right, f"2", stream);
			ins = f"<1> %vr{left} | <2> %vr{right}";
		
		case "f2i":
			inner,  = self.ins;
			connect_param(inner, f"1", stream);
			ins = f"<1> %vr{inner}";
		
		case "fload":
			address, = self.ins;
			connect_param(address, f"1", stream);
			ins = f"<1> %vr{address}";
		
		case "fadd":
			left, right = self.ins;
			connect_param(left, f"1", stream);
			connect_param(right, f"2", stream);
			ins = f"<1> %vr{left} | <2> %vr{right}";
		
		case "fmult":
			left, right = self.ins;
			connect_param(left, f"1", stream);
			connect_param(right, f"2", stream);
			ins = f"<1> %vr{left} | <2> %vr{right}";
		
		case "i2f":
			inner,  = self.ins;
			connect_param(inner, f"1", stream);
			ins = f"<1> %vr{inner}";
		
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
		
		case "icall":
			ins = f"{self.label}";
			for i, param in enumerate(self.ins):
				port = f"{i + 1}"
				connect_param(param, port, stream);
				ins += f" | <{port}> %vr{param}";
		
		case "iread":
			inner,  = self.ins;
			connect_param(inner, f"1", stream);
			ins = f"<1> %vr{inner}";
		
		case "iret":
			inner,  = self.ins;
			connect_param(inner, f"1", stream);
			ins = f"<1> %vr{inner}";
		
		case "iwrite":
			inner,  = self.ins;
			connect_param(inner, f"1", stream);
			ins = f"<1> %vr{inner}";
		
#		case "jumpI":
#			inner,  = self.ins;
#			ins = f"<1> {inner}";
		
		case "load":
			address, = self.ins;
			connect_param(address, f"1", stream);
			ins = f"<1> %vr{address}";
		
		case "loadAI":
			base, offset = self.ins;
			connect_param(base, f"1", stream);
			ins = f"<1> %vr{base} | <2> {offset}";
		
		case "loadAO":
			left, right = self.ins;
			connect_param(left, f"1", stream);
			connect_param(right, f"2", stream);
			ins = f"<1> %vr{left} | <2> %vr{right}";
		
		case "loadI":
			literal,  = self.ins;
			match literal:
				case Constant():
					ins = f"<1> {literal.value}"
				case str():
					ins = f"<1> {literal}"
				case _:
					assert(not "TODO");
		
		case "mod":
			dprint(f"self.ins = {self.ins}");
			left, right = self.ins;
			connect_param(left, f"1", stream);
			connect_param(right, f"2", stream);
			ins = f"<1> %vr{left} | <2> %vr{right}";
		
		case "mult":
			left, right = self.ins;
			connect_param(left, f"1", stream);
			connect_param(right, f"2", stream);
			ins = f"<1> %vr{left} | <2> %vr{right}";
		
		case "multI":
			value, const = self.ins;
			connect_param(value, f"1", stream);
			ins = f"<1> %vr{value} | <2> {const}";
		
		case "not":
			inner,  = self.ins;
			connect_param(inner, f"1", stream);
			ins = f"<1> %vr{inner}";
		
		case "or":
			left, right = self.ins;
			connect_param(left, f"1", stream);
			connect_param(right, f"2", stream);
			ins = f"<1> %vr{left} | <2> %vr{right}";
		
		case "ret":
			ins = ""
		
		case "store":
			value, dest = self.ins;
			connect_param(value, f"1", stream);
			connect_param(dest,  f"2", stream);
			ins = f"<1> %vr{value} | <2> %vr{dest}";
		
		case "storeAI":
			value, dest, offset = self.ins;
			connect_param(value, f"1", stream);
			connect_param(dest,  f"2", stream);
			ins = f"<1> %vr{value} | <2> %vr{dest} | <3> {offset}";
		
		case "storeAO":
			value, dest, offset = self.ins;
			connect_param(value, f"1", stream);
			connect_param(dest,  f"2", stream);
			connect_param(offset,  f"3", stream);
			ins = f"<1> %vr{value} | <2> %vr{dest} | <3> %vr{offset}";
		
		case "sub":
			left, right = self.ins;
			connect_param(left, f"1", stream);
			connect_param(right, f"2", stream);
			ins = f"<1> %vr{left} | <2> %vr{right}";
		
		case "swrite":
			inner,  = self.ins;
			connect_param(inner, f"1", stream);
			ins = f"<1> %vr{inner}";
		
		case "rshiftI":
			value, const = self.ins;
			connect_param(value, f"1", stream);
			ins = f"<1> %vr{value} | <2> {const}";
		
		case "putchar":
			inner,  = self.ins;
			connect_param(inner, f"1", stream);
			ins = f"<1> %vr{inner}";
		
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






















