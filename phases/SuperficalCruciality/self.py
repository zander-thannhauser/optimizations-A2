
from phases.self import Phase;

class SuperficalCruciality(Phase): pass;

from .init import SuperficalCruciality_init;
from .str import SuperficalCruciality_str;
from .lt import SuperficalCruciality_lt;

from .dotout import SuperficalCruciality_dotout;
from .process import SuperficalCruciality_process;

SuperficalCruciality.__init__ = SuperficalCruciality_init;
SuperficalCruciality.__str__ = SuperficalCruciality_str;
SuperficalCruciality.__lt__ = SuperficalCruciality_lt;

SuperficalCruciality.dotout = SuperficalCruciality_dotout;
SuperficalCruciality.process = SuperficalCruciality_process;


