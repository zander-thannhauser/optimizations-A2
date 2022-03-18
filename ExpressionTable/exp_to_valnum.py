
from debug import *;

def ExpressionTable_exp_to_valnum(self, expression):
	enter(f"exp_to_valnum(expression = {expression})");
	
	if expression in self.expression_to_valnum:
		retval = self.expression_to_valnum[expression];
	else:
		retval = self.valcounter;
		self.expression_to_valnum[expression] = self.valcounter;
		self.valnum_to_expression[retval] = expression;
		self.valcounter += 1;
	
	exit(f"return {retval}");
	return retval;




