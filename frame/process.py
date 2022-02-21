
# from stdio import printf, puts;

#from Instruction import Instruction;
#from Block import Block;

from .read_block import read_block;

from .dotout.control import dotout_control;
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
	
	# build dominator tree:
	assert(not "TODO");
	
	# calculate dominator frontiner
	assert(not "TODO");
	
	# global_expressions = ExpressionTable();
	assert(not "TODO");
	
	# determine the needs and provides for each block
	assert(not "TODO");
	
	# for each block:
		# number each of the provides ("%%vr%i_%i", _, id(block))
	
	assert(not "TODO");
	
	# for each block:
		# if block as no parents:
			# pass
		# elif block has one parent:
			# for each need:
				# ask parent for need, save response
		# else:
			# for each need:
				# phi = set()
				# for each parent:
					# phi.add(parent.get(need))
				# if len(phi) ==1:
					# save as thing
				# elif not new phi?
					# save as chached phi
				# else:
					# make and save new phi
			
	assert(not "TODO");
	
	dotout_data(all_blocks);
	assert(not "CHECK");
	
	# for each block: (parents then children on dominator tree)
		# block.expressions = immedate-dominator.expressions.copy();
		# block.optimize();
	assert(not "TODO");
	
	# dot out (show provides and needs)
	assert(not "TODO");
	
	# print out assembly:
	# all_blocks[0].print_asm(set());
	assert(not "TODO");
	

































