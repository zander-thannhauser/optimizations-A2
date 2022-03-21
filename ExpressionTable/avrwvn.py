
from debug import *;

def ExpressionTable_avrwvn(self, vr, vn):
	enter(f"ExpressionTable.avrwvn(vr = {vr}, vn = {vn})");
	self.vreg_to_valnum[vr] = vn;
	dprint(f"self.vreg_to_valnum[{vr}] = {self.vreg_to_valnum[vr]}");
	exit(f"return {vn};");
	return vn;



