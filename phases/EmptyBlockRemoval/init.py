
from phases.self import Phase;

def EmptyBlockRemoval_init(self, block):
	Phase.__init__(self, Phase.EMPTY_BLOCK_REMOVAL);
	self.block = block;


