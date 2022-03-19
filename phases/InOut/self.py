
from phases.self import Phase;

class InOutPhase(Phase): pass;

from .init import InOutPhase_init;
from .str import InOutPhase_str;
from .lt import InOutPhase_lt;
from .eq import InOutPhase_eq;

from .dotout import InOutPhase_dotout;
from .process import InOutPhase_process;

InOutPhase.__init__ = InOutPhase_init;
InOutPhase.__str__ = InOutPhase_str;
InOutPhase.__lt__ = InOutPhase_lt;
InOutPhase.__eq__ = InOutPhase_eq;

InOutPhase.dotout = InOutPhase_dotout;
InOutPhase.process = InOutPhase_process;


