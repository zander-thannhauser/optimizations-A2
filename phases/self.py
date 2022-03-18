
class Phase:
	counter = 0;
	ATTRIBUTES = 1;
	INHERITANCE = 2;

from .init import Phase_init;

Phase.__init__ = Phase_init;

