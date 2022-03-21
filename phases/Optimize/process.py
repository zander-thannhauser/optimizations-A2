
from debug import *;

from .self import OptimizePhase;

from .instructions.add    import optimize_add;
from .instructions.cbr    import optimize_cbr;
from .instructions.cbrne  import optimize_cbrne;
from .instructions.comp   import optimize_comp;
from .instructions.i2i    import optimize_i2i;
from .instructions.loadI  import optimize_loadI;
from .instructions.mult   import optimize_mult;
from .instructions.load   import optimize_load;
from .instructions.nop    import optimize_nop;
from .instructions.sub    import optimize_sub;
from .instructions.store  import optimize_store;
from .instructions.testeq import optimize_testeq;
from .instructions.testne import optimize_testne;
from .instructions.testgt import optimize_testgt;
from .instructions.testlt import optimize_testlt;
from .instructions.testle import optimize_testle;
from .instructions.iwrite import optimize_iwrite;
from .instructions.jumpI  import optimize_jumpI;
from .instructions.ret    import optimize_ret;

from Instruction.self import Instruction;
from ExpressionTable.Phi.self import Phi;

lookup = {
	"add":    optimize_add,
	"cbr":    optimize_cbr,
	"cbrne":  optimize_cbrne,
	"comp":   optimize_comp,
	"i2i":    optimize_i2i,
	"loadI":  optimize_loadI,
	"mult":   optimize_mult,
	"load":   optimize_load,
	"nop":    optimize_nop,
	"store":  optimize_store,
	"sub":    optimize_sub,
	"testeq": optimize_testeq,
	"testne": optimize_testne,
	"testgt": optimize_testgt,
	"testlt": optimize_testlt,
	"testle": optimize_testle,
	"iwrite": optimize_iwrite,
	"jumpI":  optimize_jumpI,
	"ret":    optimize_ret,
};

def OptimizePhase_process(self, all_blocks, expression_table, **_):
	enter(f"OptimizePhase.process(self.block.rpo = {self.block.rpo})");
	
	block = self.block;
	
	if block == all_blocks[0]:
		block.expression_table = expression_table.copy();
		
		for register in ["%vr0", "%vr1", "%vr2", "%vr3"]:
			valnum = expression_table.mkvn();
			block.expression_table.avrwvn(register, valnum);
		
		# this is also where block labels are introduced, using loadIs.
		# assert(not "TODO");
		
	else:
		block.expression_table = block.immedate_dominator.expression_table.copy();
		
		# incoming_phis is only filled with Phi's.
		for register, valnum in block.incoming_phis.items():
			# if type(expression_table.vntoex(valnum)) is Phi:
				block.expression_table.avrwvn(register, valnum);
		
		new_instructions = [];
		
		for instruction in block.instructions:
			dprint(instruction);
			lookup[instruction.op]( \
				ops = new_instructions, \
				et = block.expression_table, \
				ins = instruction.ins, \
				out = instruction.out)
		
		jump = new_instructions.pop();
		
		# ask expression_table for the value number behind each of the
		# phi-nodes-that-I-feed's virtual registers, then
		# new_instructions.append(those i2is);
		for phi_num in block.outgoing_phis:
			dprint(f"phi_num = {phi_num}");
			phi = block.expression_table.vntoex(phi_num);
			valnum = block.expression_table.vrtovn(phi.register);
			i2i = Instruction("i2i", [valnum], [phi_num]);
			new_instructions.append(i2i);
		
		before = block.instructions[-1].op;
		after = jump.op;
		
		match (before, after):
			
			case _ if before == after: pass;
			
			case ("cbr", "cbr_GT"): pass;
			case ("cbr", "cbr_NE"): pass;
			
			case ("cbr", "cbrne"): pass;
			
			case ("cbrne", "cbr"): pass;
			case ("cbrne", "cbr_GT"): pass;
			case ("cbrne", "cbr_NE"): pass;
			
			case _:
				dprint(f"block.instructions[-1].op = {block.instructions[-1].op}");
				dprint(f"jump.op = {jump.op}");
				assert(not "TODO");
		
		new_instructions.append(jump);
		
		# the paperwork for the expression_table will be handled at the usages'
		# blocks. Inserting these i2i's will just be for the assembly.
		# Globals work themselves out, only Phi nodes need this done.
		# can't put the i2i's at the *very* end, you want one before the jump
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



















