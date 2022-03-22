
from phases.self import Phase;

class EmptyBlockRemoval(Phase): pass;

from .init import EmptyBlockRemoval_init;
from .str import EmptyBlockRemoval_str;
from .lt import EmptyBlockRemoval_lt;

from .dotout import EmptyBlockRemoval_dotout;
from .process import EmptyBlockRemoval_process;

EmptyBlockRemoval.__init__ = EmptyBlockRemoval_init;
EmptyBlockRemoval.__str__ = EmptyBlockRemoval_str;
EmptyBlockRemoval.__lt__ = EmptyBlockRemoval_lt;

EmptyBlockRemoval.dotout = EmptyBlockRemoval_dotout;
EmptyBlockRemoval.process = EmptyBlockRemoval_process;


