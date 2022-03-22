
from sys import argv;

from stdio import fprintf, stderr;

from heapq import heappop, heappush;

from Instruction.self import Instruction;

from Block.self import Block;

from block import read_block;

from phases.Attribute.self import AttributePhase;
from phases.InOut.self import InOutPhase;
from phases.Inheritance.self import InheritancePhase;
from phases.Phi.self import PhiPhase;
from phases.ImmediateDominator.self import ImmediateDominatorPhase;
from phases.Optimize.self import OptimizePhase;
from phases.SuperficalCruciality.self import SuperficalCruciality;
from phases.DeadCodeRemoval.self import DeadCodeRemoval;
from phases.EmptyBlockRemoval.self import EmptyBlockRemoval;

from ExpressionTable.self import ExpressionTable;

from debug import *;

def setup_start_block(t, p, et):
	assert(t.token == ".frame");
	
	name = next(t);
	assert(next(t) == ',');
	framesize = next(t);
	
	vr_args = [];
	
	while next(t) == ",":
		reg = next(t);
		assert(reg[:3] == "%vr");
		vr_args.append(reg);
	
	vn_args = [];
	
	magic_provides = ["%vr0", "%vr1", "%vr2", "%vr3"] + vr_args;
	
	for register in magic_provides:
		valnum = et.mkvn();
		vn_args.append(valnum);
		et.avrwvn(register, valnum);
	
	p.printf(".frame %s, %s %s", name, framesize, "".join(f", %vr{vn}" for vn in vn_args[4:]), prefix = "");
	
	# frame = Instruction(".frame", [name, framesize, *args], []);
	start = Block("(.frame)", [], ["(fallthrough)"]);
	
	start.magic_provides = magic_provides;
	
	return start;

def setup_end_block():
	ret = Instruction("ret", [], []);
	end = Block("(return)", [], [], ret);
	return end;

def read_all_blocks(t, start, exit):
	all_blocks = [];
	
	all_blocks.append(start);
	
	while t.token and t.token != ".frame":
		b = read_block(t);
		all_blocks.append(b);
	
	all_blocks.append(exit);
	
	return all_blocks;

def resolve_references(all_blocks):
	enter("resolve_references()");
	
	blocks_by_name = {};
	
	for b in all_blocks:
		if b.label:
			blocks_by_name[b.label] = b;
	
	for i, b in enumerate(all_blocks):
		children = [];
		dprint(f"i = {i}");
		dprint(f"b.children_labels = {b.children_labels}");
		for c in b.children_labels:
			if c == "(fallthrough)":
				children.append(all_blocks[i + 1]);
			elif c in blocks_by_name:
				children.append(blocks_by_name[c]);
			else:
				fprintf(stderr, "%s: unresolved reference to '%s'!\n", argv[0], c);
				sys.exit(1);
		for c in children:
			c.parents.append(b);
		b.children = children;
	
	exit("return;");


po_counter = 1;

def postorder_rank(b):
	global po_counter;
	if b.po: return;
	b.po = 1;
	for c in b.children: postorder_rank(c);
	b.po = po_counter;
	po_counter += 1;

rpo_counter = 1;

def reverse_postorder_rank(b):
	global rpo_counter;
	if b.rpo: return;
	b.rpo = 1;
	for c in b.parents: reverse_postorder_rank(c);
	b.rpo = rpo_counter;
	rpo_counter += 1;

def print_asm(block, p):
	enter(f"print_asm(block.rpo = {block.rpo})");
	
	p.comment("block.rpo = %i:", block.rpo);
	
	if block.label:
		p.printf("%s:", block.label, prefix = "");
	
	for inst in block.instructions:
		inst.print(p);
	
	if block.jump is not None:
		block.jump.print(p);
	
	for i, child in enumerate(block.children):
		
		dprint(f"children[{i}] = {child}");
		
		match (i, "printed-assembly" in child.has_done):
			
			# fallthrough child, assembly already printed
			case (0, True):
				assert(not "JumpI {child}");
			
			# not fallthrough, assembly already printed
			case (_, True):
				pass;
			
			# any child with assembly that has yet to print:
			case (_, False):
				child.has_done.add("printed-assembly");
				print_asm(child, p);
			
			case conditions:
				dprint(f"conditions = {conditions}");
				assert(not "TODO");
	
	exit("return;");

def process_frame(t, p):
	
	enter("process_frame");
	
	et = ExpressionTable();
	
	start = setup_start_block(t, p, et);
	
	end = setup_end_block();
	
	all_blocks = read_all_blocks(t, start, end);
	
	resolve_references(all_blocks);
	
	postorder_rank(start);
	
	reverse_postorder_rank(end);
	
	todo = [
		## LostParentBlock()            # top-down
		AttributePhase(start),          # top-down
		InOutPhase(end),                # bottom-up
		InheritancePhase(start),        # top-down
		PhiPhase(start),                # top-down
		ImmediateDominatorPhase(start), # top-down
		OptimizePhase(start),           # top-down
		SuperficalCruciality(start),    # top-down
		## BlockCruciality(),           # bottom-up
		## InstructionCruciality(),     # bottom-up
		DeadCodeRemoval(start),         # top-down
		EmptyBlockRemoval(start),       # top-down
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
			if me not in todo:
				heappush(todo, me);
	
	p.indent();
	print_asm(all_blocks[0], p);
	p.unindent();
	
	exit("process_frame");
	

































