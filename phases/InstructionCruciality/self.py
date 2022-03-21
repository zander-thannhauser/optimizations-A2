
from phases.self import Phase;

class InstructionCruciality(Phase): pass;

from .init import InstructionCruciality_init;
from .str import InstructionCruciality_str;
from .lt import InstructionCruciality_lt;

from .dotout import InstructionCruciality_dotout;
from .process import InstructionCruciality_process;

InstructionCruciality.__init__ = InstructionCruciality_init;
InstructionCruciality.__str__ = InstructionCruciality_str;
InstructionCruciality.__lt__ = InstructionCruciality_lt;

InstructionCruciality.dotout = InstructionCruciality_dotout;
InstructionCruciality.process = InstructionCruciality_process;


