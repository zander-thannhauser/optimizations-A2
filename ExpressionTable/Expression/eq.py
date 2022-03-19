
from ExpressionTable.Expression.self import Expression;

def Expression_eq(self, other):
	return True \
		and type(other) is Expression \
		and self.op == other.op \
		and self.ins == other.ins;


