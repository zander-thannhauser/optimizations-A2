
#from debug import *;

#from frame.ExpressionTable.Phi.self import Phi;

#def Block_find(self, need, expt):
#	dprint(f"Block_find(self = {self.label}, need = {need})");
#	indent();
#	match len(self.parents):
#		case 0:
#			if need in ["%vr0", "%vr1", "%vr2", "%vr3"]:
#				# vr0, vr1, vr2 and vr3
#				# should be considered provided for by the starting block
#				retval = id(self);
#			else:
#				retval = None;
#		case 1:
#			retval = self.parents[0].provide(need, expt)
#		case _:
#			provides = set([p.provide(need, expt) for p in self.parents])
#			if None in provides: provides.remove(None);
#			dprint(f"provides = {provides}");
#			match len(provides):
#				case 0:
#					retval = None;
#				case 1:
#					# assert(not "CHECK");
#					# print(f"provides = {list(provides)[0]}");
#					retval = list(provides)[0];
#				case _:
#					# lookup phi node in expression table,
#					# create a new one if non-existant
#					retval = expt.exp_to_valnum(Phi(need, provides));
#					# return it
#	dprint(f"return {retval}");
#	unindent();
#	return retval;

#def Block_provide(self, need, expt):
#	dprint(f"Block_provide(self = {self.label}, need = {need})");
#	indent();
#	if need in self.provides:
#		retval = self.provides[need];
#	else:
#		self.provides[need] = None;
#		retval = Block_find(self, need, expt);
#		self.provides[need] = retval;
#	dprint(f"return {retval}");
#	unindent();
#	return retval;

















