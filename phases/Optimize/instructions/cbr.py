
from debug import *;

from .common import load_literal;
from .common import consider;

from Instruction.self import Instruction;

from ExpressionTable.Constant.self import Constant;
from ExpressionTable.Expression.self import Expression;

def optimize_cbr(ops, et, ins, out, label, volatile):
	enter(f"optimize_cbr(ins = {ins}, out = {out})");
	
	ivn = et.vrtovn(ins[0]);
	
	match (et.vntoex(ivn)):
		# constant-folding:
		case Constant(value = c):
			if c: ops.append(Instruction("jumpI", [], out, label));
		
		case Expression(op = "cmp_LT", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			ops.append(Instruction("cbr_LT", [X, Y], out, label));
		
		case Expression(op = "cmp_LE", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			ops.append(Instruction("cbr_LE", [X, Y], out, label));
		
		case Expression(op = "cmp_GT", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			ops.append(Instruction("cbr_GT", [X, Y], out, label));
		
		case Expression(op = "cmp_GE", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			ops.append(Instruction("cbr_GE", [X, Y], out, label));
		
		case Expression(op = "cmp_EQ", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			# ops.append(("cbr_EQ", [X, Y], "->", outs));
			assert(not "TODO");
		
		case Expression(op = "cmp_NE", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			# ops.append(("cbr_NE", [X, Y], "->", outs));
			assert(not "TODO");
		
		case Expression(op = "testeq", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			assert(not "TODO");
		
		case Expression(op = "testne", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			assert(not "TODO");
		
		case Expression(op = "testgt", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			assert(not "TODO");
		
		case Expression(op = "testge", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			assert(not "TODO");
		
		case Expression(op = "testlt", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			assert(not "TODO");
		
		case Expression(op = "testle", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			assert(not "TODO");
		
		case Expression(op = "not", ins = [X]) \
			if X not in volatile:
			ops.append(Instruction("cbrne", [X], out, label));
		
		# default:
		case iex:
			ops.append(Instruction("cbr", [ivn], out, label));
	

	exit("return;");












