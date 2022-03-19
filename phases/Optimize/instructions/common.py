
from Instruction.self import Instruction;

from ExpressionTable.Expression.self import Expression;
from ExpressionTable.Constant.self import Constant;

from debug import *;

def consider(ops, et, op, ins, out = None):
	exp = Expression(op = op, ins = ins);
	
	result = et.extovn(exp);
	
	if result.is_new:
		inst = Instruction(op, ins, result.valnum);
		ops.append(inst);
	
	if out is not None:
		et.avrwvn(out, result.valnum);
	
	return result.valnum;


def load_literal(ops, et, literal, out = None):
	enter(f"load_literal(literal = {literal})");
	
	const = Constant(literal);
	
	result = et.extovn(const);
	
	if result.is_new:
		ops.append(Instruction("loadI", [const], result.valnum));
	
	if out is not None:
		et.avrwvn(out, result.valnum);
	
	exit(f"return {result.valnum};");
	return result.valnum;

