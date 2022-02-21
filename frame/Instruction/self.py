
class Instruction: pass;

from .init import Instruction_init;
from .print import Instruction_print;

Instruction.__init__ = Instruction_init;

Instruction.print = Instruction_print;

