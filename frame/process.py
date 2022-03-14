
# from stdio import printf, puts;

#from Instruction import Instruction;
#from Block import Block;

from .read_block import read_block;

#from .calc_dominators import calc_dominators;
from .calc_immediate_dominators import calc_immediate_dominators;
from .calc_data_flow import calc_data_flow;

from .build_phi_nodes import build_phi_nodes;

from .ExpressionTable.self import ExpressionTable;

from .dotout.control import dotout_control;
from .dotout.idoms import dotout_idoms;
from .dotout.data import dotout_data;

def process_frame(t, p):
	assert(t.token == ".frame");
	
	name = next(t);
	assert(next(t) == ',');
	framesize = next(t);
	
	args = [];
	
	while next(t) == ",":
		reg = next(t);
		printf("arg += \"%s\"\n", reg);
		assert(reg[:3] == "%vr");
		args.append(reg);
	
	p.asm(".frame", [name, framesize], prefix = "");
	
	all_blocks = [];
	blocks_by_name = {};
	
	assert(not "add start block");
	
	# read blocks:
	while t.token and t.token != ".frame":
		b = read_block(t);
		all_blocks.append(b);
		if b.label:
			assert(b.label not in blocks_by_name);
			blocks_by_name[b.label] = b;
	
#	assert(not "add return block");
#	
#	# resolve references:
#	for i, b in enumerate(all_blocks):
#		children = [];
#		for c in b.children:
#			if c is "fallthrough":
#				children.append(all_blocks[i + 1]);
#			elif c is "return":
#				assert(not "TODO");
#			elif c in blocks_by_name:
#				children.append(blocks_by_name[c]);
#			else:
#				fprintf(stderr, "%s: unresolved reference to '%s'!\n", argv0, c);
#				exit(1);
#		for c in children:
#			c.parents.append(b);
#		b.children = children;
#	
#	start.idom = start;
#	start.expression_tables = ExpressionTable();
	
	# fill start.expression_tables with vr{0,1,2,3} and parameters
	
	# rank should be assigned so that blocks would be traversed
	# in reverse postorder
	
	# push phase 1, 2, 3, 4, 5 on start block
	
	# heap(key = (phase, rank))
	
	# phase 0:
		# I lost a parent
		# if self has any remaining parents:
			# push block into doing phase 1
			# push block's parents into doing phase 2
			# increment phase 3 counter
			# push block into doing phase 3
		# otherwise:
			# I'm unreachable
			# for each child:
				# self.children.remove(block)
				# block.parents.remove(self)
				# push child ininto doinging phase 0
	# phase 1:
		# assert(not unreachable)
		# if self.i2is not defined (or None):
			# skim my `i2i`s and save to self.i2is
		# pass subscripted registers to children's inputs:
		# if changed:
			# push children into doing phase 1
	# phase 2:
		# assert(not unreachable)
		# (most) parents (need to) already have their idoms
		# so I'm going to traverse upwards and figure out mine
		# if changed:
			# push children into doing phase 2
	# phase 3:
		# assert(not unreachable)
		# push children into doing phase 3
		# turn my block inputs (sets or ints) into value numbers
		# A1 optimization
		# if the conditional branch changed
			# self.children.remove(block)
			# block.parents.remove(self)
			# push block into doing phase 0
	# phase 4:
		# assert(not unreachable)
		# output assembly for this block with a child afterwards
	
	assert(not "TODO");
	
##	dotout_control(all_blocks);
##	assert(not "CHECK");
#	
#	calc_immediate_dominators(all_blocks);
##	calc_dominance_frontiers(all_blocks);
#	
##	dotout_idoms(all_blocks);
##	assert(not "CHECK");
#	
#	global_expressions = ExpressionTable();
#	
#	for b in all_blocks: b.skim_i2is();
#	
#	calc_data_flow(all_blocks);
#	
#	build_phi_nodes(all_blocks, global_expressions);
#	
#	dotout_data(all_blocks, global_expressions);
#	assert(not "CHECK");
#	
#	# for each block: (parents then children on dominator tree)
#		# block.expressions = immedate-dominator.expressions.copy();
#			# if start block: use global_expressions instead
#		# block.optimize();
#	assert(not "TODO");
#	
#	# dot out (show provides and needs)
#	assert(not "TODO");
#	
#	# print out assembly:
#	# all_blocks[0].print_asm(set());
#	assert(not "TODO");
	

































