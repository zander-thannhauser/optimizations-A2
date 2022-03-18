
from phases.self import Phase;

def AttributePhase_init(self, block):
	Phase.__init__(self, Phase.ATTRIBUTES);
	self.block = block;


