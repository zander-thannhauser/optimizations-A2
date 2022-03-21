
from phases.self import Phase;

def BlockCruciality_init(self, block):
	Phase.__init__(self, Phase.BLOCK_CRUCIALITY);
	self.block = block;


