
def Block_init(self, label, instructions, children):
	self.label = label;
	self.instructions = instructions;
	
	self.parents = [];
	self.children = children;
	
	self.changes = [];
	
