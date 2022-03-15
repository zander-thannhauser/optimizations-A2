
class Global: pass;

from .init import Global_init;
from .str import Global_str;
from .hash import Global_hash;
from .eq import Global_eq;

Global.__eq__ = Global_eq;
Global.__init__ = Global_init;
Global.__str__ = Global_str;
Global.__hash__ = Global_hash;



