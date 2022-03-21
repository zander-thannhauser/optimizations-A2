
from phases.self import Phase;

def InstructionCruciality_init(self, instruction, block):
	Phase.__init__(self, Phase.INSTRUCTION_CRUCIALITY);
	
	self.instruction = instruction;
	self.block = block;


