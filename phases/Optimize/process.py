
from debug import *;

from .self import OptimizePhase;

from .instructions.loadI  import optimize_loadI;
from .instructions.i2i    import optimize_i2i;
from .instructions.add    import optimize_add;
from .instructions.sub    import optimize_sub;
from .instructions.mult   import optimize_mult;
from .instructions.store  import optimize_store;
from .instructions.load   import optimize_load;
from .instructions.comp   import optimize_comp;
from .instructions.testeq import optimize_testeq;
from .instructions.cbr    import optimize_cbr;

lookup = {
	"loadI":  optimize_loadI,
	"i2i":    optimize_i2i,
	"add":    optimize_add,
	"sub":    optimize_sub,
	"mult":   optimize_mult,
	"store":  optimize_store,
	"load":   optimize_load,
	"comp":   optimize_comp,
	"testeq": optimize_testeq,
	"cbr":    optimize_cbr,
};

def OptimizePhase_process(self, all_blocks, expression_table, **_):
	enter(f"OptimizePhase.process(self.block.rpo = {self.block.rpo})");
	
	block = self.block;
	
	if block == all_blocks[0]:
		block.expression_table = expression_table.copy();
	else:
		block.expression_table = block.immedate_dominator.expression_table.copy();
	
	for register, valnum in block.given_valnums.items():
		block.expression_table.avrwvn(register, valnum);
	
	new_instructions = [];
	
	for instruction in block.instructions:
		dprint(f"{str(instruction)}");
		lookup[instruction.op]( \
			ops = new_instructions, \
			et = block.expression_table, \
			ins = instruction.ins, \
			out = instruction.out)
	
	# we can't remove useless instructions, because maybe other blocks
	# use them
	
	# ask expression_table for the value number behind each of my global's
	# virtual register, then new_instructions.append(those i2is);
	# can't put them at the *very* end, you want one before the jump
	# instruction.
	# assert(not "TODO");
	
	block.instructions = new_instructions;
	
	block.has_done.add("optimized");
	
	todo = [];
	
	for child in block.children:
		if "will-optimize" not in child.has_done:
			todo.append(OptimizePhase(child));
			child.has_done.add("will-optimize");
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;



















