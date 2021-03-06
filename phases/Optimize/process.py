
from debug import *;

from .self import OptimizePhase;

from .instructions.add     import optimize_add;
from .instructions.call    import optimize_call;
from .instructions.cbr     import optimize_cbr;
from .instructions.cbrne   import optimize_cbrne;
from .instructions.comp    import optimize_comp;
from .instructions.f2i     import optimize_f2i;
from .instructions.fadd    import optimize_fadd;
from .instructions.fload   import optimize_fload;
from .instructions.fmult   import optimize_fmult;
from .instructions.i2f     import optimize_i2f;
from .instructions.i2i     import optimize_i2i;
from .instructions.icall   import optimize_icall;
from .instructions.iread   import optimize_iread;
from .instructions.iret    import optimize_iret;
from .instructions.loadI   import optimize_loadI;
from .instructions.mod     import optimize_mod;
from .instructions.mult    import optimize_mult;
from .instructions.load    import optimize_load;
from .instructions.nop     import optimize_nop;
from .instructions._or     import optimize_or;
from .instructions.putchar import optimize_putchar;
from .instructions.rshift  import optimize_rshift;
from .instructions.sub     import optimize_sub;
from .instructions.store   import optimize_store;
from .instructions.testeq  import optimize_testeq;
from .instructions.testne  import optimize_testne;
from .instructions.testge  import optimize_testge;
from .instructions.testgt  import optimize_testgt;
from .instructions.testlt  import optimize_testlt;
from .instructions.testle  import optimize_testle;
from .instructions.iwrite  import optimize_iwrite;
from .instructions.jumpI   import optimize_jumpI;
from .instructions.ret     import optimize_ret;
from .instructions.swrite  import optimize_swrite;

from Instruction.self import Instruction;
from ExpressionTable.Phi.self import Phi;
from ExpressionTable.Constant.self import Constant;

lookup = {
	"add":     optimize_add,
	"call":    optimize_call,
	"cbr":     optimize_cbr,
	"cbrne":   optimize_cbrne,
	"comp":    optimize_comp,
	"f2i":     optimize_f2i,
	"fadd":    optimize_fadd,
	"fload":   optimize_fload,
	"fmult":   optimize_fmult,
	"i2f":     optimize_i2f,
	"i2i":     optimize_i2i,
	"icall":   optimize_icall,
	"iread":   optimize_iread,
	"iret":    optimize_iret,
	"loadI":   optimize_loadI,
	"mod":     optimize_mod,
	"mult":    optimize_mult,
	"load":    optimize_load,
	"nop":     optimize_nop,
	"or":      optimize_or,
	"putchar": optimize_putchar,
	"rshift":  optimize_rshift,
	"store":   optimize_store,
	"sub":     optimize_sub,
	"testeq":  optimize_testeq,
	"testne":  optimize_testne,
	"testgt":  optimize_testgt,
	"testge":  optimize_testge,
	"testlt":  optimize_testlt,
	"testle":  optimize_testle,
	"iwrite":  optimize_iwrite,
	"jumpI":   optimize_jumpI,
	"ret":     optimize_ret,
	"swrite":  optimize_swrite,
};

def OptimizePhase_process(self, all_blocks, expression_table, **_):
	enter(f"OptimizePhase.process(self.block.rpo = {self.block.rpo})");
	
	block = self.block;
	
	if block == all_blocks[0]:
		block.expression_table = expression_table.copy();
		
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
				out = instruction.out, \
				label = instruction.label)
		
		volatile_registers = set();
		
		# ask expression table for the value number behind each of the
		# phi-nodes-that-I-feed's virtual registers, then
		# new_instructions.append(those i2is);
		
		for out_reg in block.outs:
			if out_reg in block.outgoing_phis:
				src_valnum = block.expression_table.vrtovn(out_reg);
				dst_valnum = block.outgoing_phis[out_reg];
				dprint(f"dst_valnum, src_valnum = {dst_valnum, src_valnum}");
#				match block.expression_table.vntoex(src_valnum):
#					case Constant() as c:
#						appendme = Instruction("loadI", [c], dst_valnum);
#					case _:
#						appendme = Instruction("i2i", [src_valnum], dst_valnum);
				appendme = Instruction("i2i", [src_valnum], dst_valnum);
				new_instructions.append(appendme);
				volatile_registers.add(dst_valnum);
		
		# it would be nice to have a second pass right here
		# for any i2is, if they are the sole user of a definition,
		# change the definition to write to the phi node, remove
		# the i2i
		# assert(not "TODO");
		
		for instruction in new_instructions:
			if type(instruction.out) is int:
				block.valnum_to_instruction[instruction.out] = instruction;
		
		if block.jump is not None:
			before = block.jump;
			
			dprint(block.jump);
			
			# wrote_i2is = len(block.outgoing_phis) > 0;
			
			lookup[before.op]( \
				ops = new_instructions, \
				et = block.expression_table, \
				ins = before.ins, \
				out = before.out, \
				label = before.label, \
				volatile = volatile_registers)
			
			after = new_instructions.pop();
			
			dprint(f"before.op, after.op = {before.op, after.op}");
			
			match (before.op, after.op):
				
				case _ if before.op == after.op: pass;
				
				case ("cbr", "cbr_GT"): pass;
				case ("cbr", "cbr_GE"): pass;
				case ("cbr", "cbr_NE"): pass;
				case ("cbr", "cbr_LE"): pass;
				case ("cbr", "cbr_LT"): pass;
				
				case ("cbr", "cbrne"): pass;
				
				case ("cbrne", "cbr"): pass;
				case ("cbrne", "cbr_GE"): pass;
				case ("cbrne", "cbr_GT"): pass;
				case ("cbrne", "cbr_NE"): pass;
				case ("cbrne", "cbr_EQ"): pass;
				case ("cbrne", "cbr_LT"): pass;
				
				# fallthrough never happens, jump always happens:
				# remove jump instruction, remove connection with fallthrough
				# TODO: and push old paperwork phases.
				
				case ('cbrne' | 'cbr', 'jumpI'):
					lose, keep = block.children;
					lose.parents.remove(block);
					block.children = [keep];
					after = None;
				
				# fallthrough always happens, jump never happens:
				# remove the jump instruction, have this block consider
				# it's one parent as it's fallthrough.
				# TODO: and push old paperwork phases.
				
				case ("cbr" | "cbrne", "i2i" | "loadI"):
					new_instructions.append(after);
					keep, lose = block.children;
					lose.parents.remove(block);
					block.children = [keep];
					after = None;
				
				case _:
					assert(not "TODO");
			
			block.jump = after;
		
		block.instructions = new_instructions;
		
		block.has_done.add("optimized");
	
	todo = [];
	
	for child in block.children:
		if "will-optimize" not in child.has_done:
			todo.append(OptimizePhase(child));
			child.has_done.add("will-optimize");
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;



















