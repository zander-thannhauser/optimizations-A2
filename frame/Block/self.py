
class Block: pass

from .init import Block_init;
from .str import Block_str;
from .print_asm import Block_print_asm;
from .optimize.optimize import Block_optimize;

Block.__init__ = Block_init;
Block.__str__ = Block_str;

Block.optimize = Block_optimize;
Block.print_asm = Block_print_asm;


