
from phases.self import Phase;

class AttributePhase(Phase): pass;

from .init import AttributePhase_init;
from .str import AttributePhase_str;
from .lt import AttributePhase_lt;

from .dotout import AttributePhase_dotout;
from .process import AttributePhase_process;

AttributePhase.__init__ = AttributePhase_init;
AttributePhase.__str__ = AttributePhase_str;
AttributePhase.__lt__ = AttributePhase_lt;

AttributePhase.dotout = AttributePhase_dotout;
AttributePhase.process = AttributePhase_process;


