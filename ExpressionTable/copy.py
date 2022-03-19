
from ExpressionTable.self import ExpressionTable;

def ExpressionTable_copy(self):
	
	copy = ExpressionTable();
	
	copy.expression_to_valnum = self.expression_to_valnum.copy();
	copy.valnum_to_expression = self.valnum_to_expression.copy();
	
	return copy;

