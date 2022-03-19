
from phases.self import Phase;

def ImmediateDominatorPhase_init(self, block):
	Phase.__init__(self, Phase.IMMEDIATE_DOMINATOR);
	self.block = block;


