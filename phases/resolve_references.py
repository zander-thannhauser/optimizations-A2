
#from .build_label_lookup import label_lookup, read_order_lookup;

#def resolve_references(block):
#	for label in block.children_labels:
#		if label == "(fallthrough)":
#			child = read_order_lookup[block.read_order + 1];
#		elif label not in label_lookup:
#			assert(not "TODO");
#		else:
#			child = label_lookup[label];
#		block.children.append(child);
#		child.parents.append(block);
#	block.children_labels = [];
#	return [(2, child) for child in block.children];


