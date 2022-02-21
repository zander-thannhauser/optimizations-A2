
def Block_init(self, label, instructions, children):
	self.label = label;
	self.instructions = instructions;
	
	self.parents = [];
	self.children = children;
	
	self.immdom = None;
	
	self.needs = {};    # register name -> subscript string
	self.provides = {}; # register name -> subscript string
	
	self.expressions = None;

