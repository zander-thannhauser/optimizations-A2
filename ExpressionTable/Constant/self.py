
class Constant: pass;

from .init import Constant_init;
from .str import Constant_str;
from .hash import Constant_hash;
from .eq import Constant_eq;

Constant.__init__ = Constant_init;
Constant.__str__ = Constant_str;
Constant.__hash__ = Constant_hash;
Constant.__eq__ = Constant_eq;




