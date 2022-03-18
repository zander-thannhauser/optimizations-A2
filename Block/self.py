
class Block: pass

from .init import Block_init;
from .str import Block_str;
from .lt import Block_lt;
from .eq import Block_eq;
from .str import Block_str;

Block.__init__ = Block_init;
Block.__str__ = Block_str;
Block.__lt__ = Block_lt;
Block.__eq__ = Block_eq;
Block.__str__ = Block_str;


