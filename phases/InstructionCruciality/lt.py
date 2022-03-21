
from debug import *;

# should the heap prioitize me over them?

def InstructionCruciality_lt(self, other):
	if self.kind < other.kind:
		return True;
	elif self.kind > other.kind:
		return False;
	else:
		match (self.instruction.out, other.instruction.out):
			
			case (_, None):
				return False;
			
			case (None, _):
				return True;
			
			case (x, y):
				return x > y;
			

