
from sys import argv;

from stdio import fprintf, stderr;

from heapq import heappop, heappush;

from Instruction.self import Instruction;

from Block.self import Block;

from block import read_block;

from phases.Attribute.self import AttributePhase;
#from phases.Inheritance.self import InheritancePhase;
#from phases.Phi.self import PhiPhase;

#from dotouts.attributes import dotout_attributes;
#from dotouts.inheritance import dotout_inheritance;
#from dotouts.phi import dotout_phi;

from ExpressionTable.self import ExpressionTable;

from debug import *;

def setup_start_block(t):
	assert(t.token == ".frame");
	
	name = next(t);
	assert(next(t) == ',');
	framesize = next(t);
	
	args = [];
	
	while next(t) == ",":
		reg = next(t);
		assert(reg[:3] == "%vr");
		args.append(reg);
	
	frame = Instruction(".frame", [name, framesize, *args], []);
	start = Block("(.frame)", [frame], ["(fallthrough)"]);
	
	start.i2is = ["%vr0", "%vr1", "%vr2", "%vr3"];
	
	return start;

def setup_end_block():
	ret = Instruction("ret", [], []);
	end = Block("(return)", [ret], []);
	return end;

def read_all_blocks(t, start, exit):
	all_blocks = [];
	
	while t.token and t.token != ".frame":
		b = read_block(t);
		all_blocks.append(b);
	
	first = all_blocks[0];
	start.children.append(first);
	first.parents.append(start);
	
	all_blocks.insert(0, start);
	all_blocks.append(exit);
	
	return all_blocks;

def resolve_references(all_blocks):
	blocks_by_name = {};
	
	for b in all_blocks:
		if b.label:
			blocks_by_name[b.label] = b;
	
	for i, b in enumerate(all_blocks):
		children = [];
		for c in b.children_labels:
			if c == "(fallthrough)":
				children.append(all_blocks[i + 1]);
			elif c in blocks_by_name:
				children.append(blocks_by_name[c]);
			else:
				fprintf(stderr, "%s: unresolved reference to '%s'!\n", argv[0], c);
				exit(1);
		for c in children:
			c.parents.append(b);
		b.children = children;

counter = 1;

def reverse_postorder_rank(b):
	global counter;
	if b.rank: return;
	b.rank = 1;
	for c in b.parents: reverse_postorder_rank(c);
	b.rank = counter;
	counter += 1;

def print_asm(p):
	assert(not "TODO");

def process_frame(t, p):
	
	enter("process_frame");
	
	start = setup_start_block(t);
	
	end = setup_end_block();
	
	all_blocks = read_all_blocks(t, start, end);
	
	resolve_references(all_blocks);
	
	reverse_postorder_rank(end);
	
	et = ExpressionTable();
	
	todo = [
		AttributePhase(start),
		# (2, start),
		# (3, start),
	];
	
	args = {
		"all_blocks": all_blocks,
		"expression_table": et,
	};
	
	if len(todo):
		todo[0].dotout(**args);
	
	while len(todo):
		# print([str(p) for p in todo]);
		
		phase = heappop(todo);
		
		addmes = phase.process(**args);
		
		phase.dotout(**args);
		
		for me in addmes:
			heappush(todo, me);
	
	exit("process_frame");
	
	# print_asm(p);
	# assert(not "TODO");
	
#	all_blocks = [];
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
	
#	assert(not "TODO");
	
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
	

































