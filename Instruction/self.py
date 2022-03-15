
class Instruction: pass;

from .init import Instruction_init;
from .print import Instruction_print;
from .str import Instruction_str;

Instruction.__init__ = Instruction_init;
Instruction.__str__ = Instruction_str;

Instruction.print = Instruction_print;

