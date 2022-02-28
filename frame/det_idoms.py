
#from misc.Empty import Empty;

#def first_pass(history, block):
#	print(f"first_pass(block = {block.label})");
#	if "det_idoms" not in vars(block):
#		block.det_idoms = Empty();
#		newhist = history + [block];
#		real_parents = [p for p in block.parents if p not in newhist];
#		for p in real_parents:
#			first_pass(newhist, p);
#		block.det_idoms.real_parents = real_parents;

#def second_pass(history, block, consider):
#	print(f"second_pass(block = {block.label}, consider = {[c.label for c in consider]})");
#	if "paths" not in vars(block.det_idoms):
#		block.det_idoms.paths = [];
#	block.det_idoms.paths.append(history);
#	i = 0; n = len(consider);
#	while i < n:
#		c = consider[i];
#		if sum(c in p for p in block.det_idoms.paths) == len(c.det_idoms.real_parents):
#			print(f"{c.label}.idom = {block.label}");
#			c.idom = block;
#			consider.pop(i);
#			n -= 1;
#		else:
#			i += 1;
#	if not vars(block.det_idoms).get("visted2", False):
#		block.det_idoms.visted2 = True;
#		if len(block.det_idoms.real_parents):
#			newhist = history + [block];
#			for p in block.det_idoms.real_parents[:-1]:
#				second_pass(newhist, p, []);
#			second_pass(newhist, block.det_idoms.real_parents[-1], consider + [block]);

#def det_idoms(all_blocks):
#	first_pass([], all_blocks[-1]);
#	
#	for b in all_blocks:
#		print(f"{b.label}: {[p.label for p in b.det_idoms.real_parents]}");
#	
#	second_pass([], all_blocks[-1], []);
