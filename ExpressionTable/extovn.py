
from debug import *;

from ExpressionTable.self import ExpressionTable;

class ExpressionTable_extovn_retval:
	def __init__(self, valnum, is_new):
		self.valnum = valnum;
		self.is_new = is_new;
	def __str__(self):
		return f"(.valnum = {self.valnum}, .is_new = {self.is_new})";

def ExpressionTable_extovn(self, expression):
	enter(f"ExpressionTable.extovn(expression = {expression})");
	
	if expression in self.expression_to_valnum:
		valnum = self.expression_to_valnum[expression];
		is_new = False;
	else:
		valnum = ExpressionTable.valcounter;
		is_new = True;
		self.expression_to_valnum[expression] = valnum;
		self.valnum_to_expression[valnum] = expression;
		ExpressionTable.valcounter += 1;
	
	retval = ExpressionTable_extovn_retval(valnum, is_new);
	
	exit(f"return {str(retval)}");
	return retval;




