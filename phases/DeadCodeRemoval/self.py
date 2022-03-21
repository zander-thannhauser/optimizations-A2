
from phases.self import Phase;

class DeadCodeRemoval(Phase): pass;

from .init import DeadCodeRemoval_init;
from .str import DeadCodeRemoval_str;
from .lt import DeadCodeRemoval_lt;

from .dotout import DeadCodeRemoval_dotout;
from .process import DeadCodeRemoval_process;

DeadCodeRemoval.__init__ = DeadCodeRemoval_init;
DeadCodeRemoval.__str__ = DeadCodeRemoval_str;
DeadCodeRemoval.__lt__ = DeadCodeRemoval_lt;

DeadCodeRemoval.dotout = DeadCodeRemoval_dotout;
DeadCodeRemoval.process = DeadCodeRemoval_process;


