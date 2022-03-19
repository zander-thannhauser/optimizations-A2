
from phases.self import Phase;

def InOutPhase_init(self, block):
	Phase.__init__(self, Phase.IN_OUT);
	self.block = block;


