
class Phi: pass;

from .init import Phi_init;
from .str import Phi_str;
from .hash import Phi_hash;
from .eq import Phi_eq;

Phi.__eq__ = Phi_eq;
Phi.__init__ = Phi_init;
Phi.__str__ = Phi_str;
Phi.__hash__ = Phi_hash;


