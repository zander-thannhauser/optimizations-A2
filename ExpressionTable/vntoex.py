
from debug import *;

def ExpressionTable_vntoex(self, vn):
	enter(f"ExpressionTable.vntoex(vn = {vn})");
	exp = self.valnum_to_expression.get(vn);
	exit(f"return {exp}");
	return exp;


