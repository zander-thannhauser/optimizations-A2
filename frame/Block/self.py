
class Block: pass

from .init import Block_init;
from .str import Block_str;
from .print_asm import Block_print_asm;
from .get_idom import Block_get_idom;
from .optimize.optimize import Block_optimize;
from .skim_i2is import Block_skim_i2is;

Block.__init__ = Block_init;
Block.__str__ = Block_str;

Block.optimize = Block_optimize;
Block.print_asm = Block_print_asm;
Block.get_idom = Block_get_idom;
Block.skim_i2is = Block_skim_i2is;


