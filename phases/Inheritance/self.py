
from phases.self import Phase;

class InheritancePhase(Phase): pass;

from .init import InheritancePhase_init;
from .str import InheritancePhase_str;
from .lt import InheritancePhase_lt;

from .dotout import InheritancePhase_dotout;
from .process import InheritancePhase_process;

InheritancePhase.__init__ = InheritancePhase_init;
InheritancePhase.__str__ = InheritancePhase_str;
InheritancePhase.__lt__ = InheritancePhase_lt;

InheritancePhase.dotout = InheritancePhase_dotout;
InheritancePhase.process = InheritancePhase_process;


