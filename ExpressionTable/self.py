
class ExpressionTable: pass

from .init import ExpressionTable_init;
from .exp_to_valnum import ExpressionTable_exp_to_valnum;
from .valnum_to_exp import ExpressionTable_valnum_to_exp;

ExpressionTable.valnum_to_exp = ExpressionTable_valnum_to_exp;
ExpressionTable.__init__ = ExpressionTable_init;
ExpressionTable.exp_to_valnum = ExpressionTable_exp_to_valnum;

