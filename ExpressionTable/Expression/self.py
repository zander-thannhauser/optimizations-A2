
class Expression: pass;

from .init import Expression_init;
from .str import Expression_str;
from .eq import Expression_eq;
from .hash import Expression_hash;

Expression.__init__ = Expression_init;
Expression.__str__ = Expression_str;
Expression.__eq__ = Expression_eq;
Expression.__hash__ = Expression_hash;



