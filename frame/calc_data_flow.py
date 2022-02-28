
def calc_data_flow(all_blocks):
	for b in all_blocks: b.givens = dict();
	
	start = all_blocks[0];
	start.givens["%vr0"] = set([0]);
	start.givens["%vr1"] = set([0]);
	start.givens["%vr2"] = set([0]);
	start.givens["%vr3"] = set([0]);
	
	todo = [start];
	while len(todo):
		print(f"todo == {[t.label for t in todo]}");
		block = todo.pop();
#		print(f"block.given == {block.given}");
#		print(f"block.changes == {block.changes}");
		newprovides = block.givens.copy();
		for p in block.changes:
			newprovides[p] = set([id(block)]);
		for c in block.children:
			changed = False;
			for p, v in newprovides.items():
				if p not in c.givens:
					# print(f"{c.label} inherited {p}");
					changed = True; c.givens[p] = v;
				elif any(V not in c.givens[p] for V in v):
					# print(f"{c.label} inherited {p}");
					changed = True; c.givens[p].update(v);
			if changed:
				todo.append(c);
	

















