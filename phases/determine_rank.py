
#def determine_rank(block):
#	if len(block.parents):
#		newrank = max(p.rank for p in block.parents) + 1;
#	else:
#		newrank = 0;
#	
#	print(f"{newrank} vs. {block.rank}");
#	
#	if newrank != block.rank:
#		block.rank = newrank;
#		return [(1, child) for child in block.children];
#	
#	return [];

