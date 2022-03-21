
from phases.self import Phase;

class BlockCruciality(Phase): pass;

from .init import BlockCruciality_init;
from .str import BlockCruciality_str;
from .lt import BlockCruciality_lt;

from .dotout import BlockCruciality_dotout;
from .process import BlockCruciality_process;

BlockCruciality.__init__ = BlockCruciality_init;
BlockCruciality.__str__ = BlockCruciality_str;
BlockCruciality.__lt__ = BlockCruciality_lt;

BlockCruciality.dotout = BlockCruciality_dotout;
BlockCruciality.process = BlockCruciality_process;


