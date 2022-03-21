
from debug import *;

from ExpressionTable.Constant.self import Constant;

from Instruction.self import Instruction;

from .common import load_literal, consider;

def optimize_loadI(ops, et, ins, out, label):
	enter(f"optimize_loadI(ins = {ins}, out = {out})");
	
	try:
		literal = int(ins[0]);
		load_literal(ops, et, literal, out);
	except ValueError:
		consider(ops, et, "loadI", (ins[0], ), out);
		# assert(not "TODO");
	
	exit("return;");



