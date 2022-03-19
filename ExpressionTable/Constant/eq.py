
from ExpressionTable.Constant.self import Constant;

def Constant_eq(self, other):
	return type(other) is Constant and self.value == other.value;




