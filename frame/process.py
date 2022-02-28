
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
	
	# read blocks:
	while t.token and t.token != ".frame":
		b = read_block(t);
		all_blocks.append(b);
		if b.label:
			assert(b.label not in blocks_by_name);
			blocks_by_name[b.label] = b;
	
	# resolve references:
	for i, b in enumerate(all_blocks):
		children = [];
		for c in b.children:
			if c is None:
				children.append(all_blocks[i + 1]);
			elif c in blocks_by_name:
				children.append(blocks_by_name[c]);
			else:
				fprintf(stderr, "%s: unresolved reference to '%s'!\n", argv0, c);
				exit(1);
		for c in children:
			c.parents.append(b);
		b.children = children;
	
#	dotout_control(all_blocks);
#	assert(not "CHECK");
	
	calc_immediate_dominators(all_blocks);
#	calc_dominance_frontiers(all_blocks);
	
#	dotout_idoms(all_blocks);
#	assert(not "CHECK");
	
	global_expressions = ExpressionTable();
	
	for b in all_blocks: b.skim_i2is();
	
	calc_data_flow(all_blocks);
	
	build_phi_nodes(all_blocks, global_expressions);
	
	dotout_data(all_blocks, global_expressions);
	assert(not "CHECK");
	
	# for each block: (parents then children on dominator tree)
		# block.expressions = immedate-dominator.expressions.copy();
			# if start block: use global_expressions instead
		# block.optimize();
	assert(not "TODO");
	
	# dot out (show provides and needs)
	assert(not "TODO");
	
	# print out assembly:
	# all_blocks[0].print_asm(set());
	assert(not "TODO");
	

































