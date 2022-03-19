
from phases.self import Phase;

class PhiPhase(Phase): pass;

from .init import PhiPhase_init;
from .str import PhiPhase_str;
from .lt import PhiPhase_lt;

from .dotout import PhiPhase_dotout;
from .process import PhiPhase_process;

PhiPhase.__init__ = PhiPhase_init;
PhiPhase.__str__ = PhiPhase_str;
PhiPhase.__lt__ = PhiPhase_lt;

PhiPhase.dotout = PhiPhase_dotout;
PhiPhase.process = PhiPhase_process;


