
class ExpressionTable:
	valcounter = 0;

from .init import ExpressionTable_init;
from .copy import ExpressionTable_copy;
from .extovn import ExpressionTable_extovn;
#from .valnum_to_exp import ExpressionTable_valnum_to_exp;
from .avrwvn import ExpressionTable_avrwvn;
from .vrtovn import ExpressionTable_vrtovn;
from .vntoex import ExpressionTable_vntoex;
from .mkvn import ExpressionTable_mkvn;

ExpressionTable.__init__ = ExpressionTable_init;
ExpressionTable.copy = ExpressionTable_copy;
#ExpressionTable.valnum_to_exp = ExpressionTable_valnum_to_exp;
ExpressionTable.extovn = ExpressionTable_extovn;
ExpressionTable.avrwvn = ExpressionTable_avrwvn;
ExpressionTable.vrtovn = ExpressionTable_vrtovn;
ExpressionTable.vntoex = ExpressionTable_vntoex;
ExpressionTable.mkvn = ExpressionTable_mkvn;
