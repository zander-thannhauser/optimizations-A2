
class Phase:
	counter = 0;
	ATTRIBUTES = 1;
	IN_OUT = 2;
	INHERITANCE = 3;
	PHI = 4;

from .init import Phase_init;

Phase.__init__ = Phase_init;

