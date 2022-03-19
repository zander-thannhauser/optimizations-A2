
from phases.self import Phase;

def OptimizePhase_init(self, block):
	Phase.__init__(self, Phase.OPTIMIZE);
	self.block = block;


