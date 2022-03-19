
from phases.self import Phase;

class ImmediateDominatorPhase(Phase): pass;

from .init import ImmediateDominatorPhase_init;
from .str import ImmediateDominatorPhase_str;
from .lt import ImmediateDominatorPhase_lt;

from .dotout import ImmediateDominatorPhase_dotout;
from .process import ImmediateDominatorPhase_process;

ImmediateDominatorPhase.__init__ = ImmediateDominatorPhase_init;
ImmediateDominatorPhase.__str__ = ImmediateDominatorPhase_str;
ImmediateDominatorPhase.__lt__ = ImmediateDominatorPhase_lt;

ImmediateDominatorPhase.dotout = ImmediateDominatorPhase_dotout;
ImmediateDominatorPhase.process = ImmediateDominatorPhase_process;


