
from phases.self import Phase;

class OptimizePhase(Phase): pass;

from .init import OptimizePhase_init;
from .str import OptimizePhase_str;
from .lt import OptimizePhase_lt;

from .dotout import OptimizePhase_dotout;
from .process import OptimizePhase_process;

OptimizePhase.__init__ = OptimizePhase_init;
OptimizePhase.__str__ = OptimizePhase_str;
OptimizePhase.__lt__ = OptimizePhase_lt;

OptimizePhase.dotout = OptimizePhase_dotout;
OptimizePhase.process = OptimizePhase_process;


