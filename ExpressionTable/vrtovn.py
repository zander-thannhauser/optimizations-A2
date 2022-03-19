
from debug import *;

def ExpressionTable_vrtovn(self, vr):
	enter(f"ExpressionTable.vrtovn(vr = {vr})");
	valnum = self.vreg_to_valnum[vr];
	exit(f"return {valnum};")
	return valnum;

