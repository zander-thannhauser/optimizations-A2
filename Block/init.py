
def Block_init(self, label, instructions, children_labels):
	self.label = label;
	self.instructions = instructions;
	
	self.parents = [];
	
	self.children = [];
	
	self.children_labels = children_labels;
	
	self.rank = 0;
	
