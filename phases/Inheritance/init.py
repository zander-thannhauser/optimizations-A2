
from phases.self import Phase;

def InheritancePhase_init(self, block):
	Phase.__init__(self, Phase.INHERITANCE);
	self.block = block;


