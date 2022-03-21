
from phases.self import Phase;

def DeadCodeRemoval_init(self, block):
	Phase.__init__(self, Phase.DEAD_CODE_REMOVAL);
	self.block = block;


