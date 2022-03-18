
def Block_init(self, label, instructions, children_labels):
	
	# used during reading assembly:
	self.label = label;
	self.instructions = instructions;
	self.children_labels = children_labels;
	
	# after reading assembly:
	self.parents = [];
	self.children = [];
	self.rank = 0;
	
	# attribute phase:
	self.attributes = {};
	self.has_done = set();
	
	# inheritance phase:
	self.given = {};
	
	# phi phase:
	self.given_valnums = {};
	
	
