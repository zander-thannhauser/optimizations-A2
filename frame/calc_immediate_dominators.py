
# from the book (page 532)

def reverse_postorder(all_blocks):
	answer = [];
	def slave(b):
		if "reverse_postorder" in vars(b): return;
		b.reverse_postorder = None;
		if b in answer: return;
		for p in b.parents: slave(p);
		answer.append(b);
	slave(all_blocks[-1])
	return answer;

def calc_immediate_dominators(all_blocks):
	rpo = reverse_postorder(all_blocks);
	for b in all_blocks:
		b.immedate_dominator = None;
	all_blocks[0].immedate_dominator = all_blocks[0];
	changed = True;
	while changed:
		changed = False;
		for b in rpo[1:]:
#			print(f"b.label = {b.label}");
			processed_predessors = [p for p in b.parents \
				if p.immedate_dominator is not None];
			new_idom = processed_predessors[0];
#			print(f"new_idom.label = {new_idom.label}");
			for p in processed_predessors[1:]:
				new_idom = intersect(p, new_idom, rpo);
#			print(f"new_idom.label = {new_idom.label}");
			if b.immedate_dominator != new_idom:
				b.immedate_dominator = new_idom;
				changed = True;


def intersect(i, j, rpo):
#	print(f"intersect(i = {i.label}, j = {j.label})");
	finger1 = i
	finger2 = j
	while finger1 != finger2:
		while rpo.index(finger1) > rpo.index(finger2):
			finger1 = finger1.immedate_dominator;
		while rpo.index(finger2) > rpo.index(finger1):
			finger2 = finger2.immedate_dominator;
	# print(f"finger1 = {finger1.label}")
	return finger1;

















