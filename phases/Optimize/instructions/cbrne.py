
from debug import *;

from .common import load_literal;
from .common import consider;

from Instruction.self import Instruction;

from ExpressionTable.Constant.self import Constant;
from ExpressionTable.Expression.self import Expression;

def optimize_cbrne(ops, et, ins, out, label, volatile):
	enter(f"optimize_cbrne(ins = {ins}, out = {out})");
	
	ivn = et.vrtovn(ins[0]);
	
	match (et.vntoex(ivn)):
		# constant-folding:
		case Constant(value = c):
			# if c: process_jumpI(ops, [], outs);
			assert(not "TODO");
		
		case Expression(op = "cmp_LT", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			ops.append(Instruction("cbr_GE", [X, Y], out, label));
		
		case Expression(op = "cmp_LE", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			assert(not "TODO");
		
		case Expression(op = "cmp_GT", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			assert(not "TODO");
		
		case Expression(op = "cmp_GE", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			assert(not "TODO");
		
		case Expression(op = "cmp_EQ", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			# check for using a move instruction's result
			ops.append(Instruction("cbr_NE", [X, Y], out, label));
		
		case Expression(op = "cmp_NE", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			# check for using a move instruction's result
			ops.append(Instruction("cbr_EQ", [X, Y], out, label));
		
		case Expression(op = "testeq", ins = [X]) \
			if X not in volatile:
			assert(not "TODO");
		
		case Expression(op = "testne", ins = [X]) \
			if X not in volatile:
			assert(not "TODO");
		
		case Expression(op = "testgt", ins = [X]) \
			if X not in volatile:
			assert(not "TODO");
		
		case Expression(op = "testge", ins = [X]) \
			if X not in volatile:
			assert(not "TODO");
		
		case Expression(op = "testlt", ins = [X]) \
			if X not in volatile:
			assert(not "TODO");
		
		case Expression(op = "testle", ins = [X]) \
			if X not in volatile:
			assert(not "TODO");
		
		case Expression(op = "and", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			assert(not "TODO");
		
		case Expression(op = "or", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			assert(not "TODO");
		
		case Expression(op = "not", ins = [X]) \
			if X not in volatile and Y not in volatile:
			# ops.append(("cbr", [X], "->", [out]));
			assert(not "TODO");
		
		# default:
		case (iex):
			dprint(f"iex == {iex}");
			# ops.append(Instruction("cbr", [ivn], out));
			assert(not "TODO");
	

	exit("return;");












