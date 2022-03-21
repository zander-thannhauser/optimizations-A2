
def Block_init(self, label, instructions, children_labels, jump = None):
	
	# used during reading assembly:
	self.label = label;
	self.instructions = instructions;
	self.jump = jump;
	self.children_labels = children_labels;
	
	# after reading assembly:
	self.parents = [];
	self.children = [];
	self.po = 0;
	self.rpo = 0;
	
	# attribute phase:
	self.attributes = {};
	self.has_done = set();
	
	# in-out phase:
	self.ins = set();
	self.outs = set();
	
	# inheritance phase:
	self.given = {};
	
	# phi phase:
	self.incoming_phis = {}; # register -> phi valnum
	self.outgoing_phis = set(); # phi valnums
	
	# immedate dominator phase:
	self.immedate_dominator = None;
	
	# optimization phase:
	self.valnum_to_instruction = {};
	
	# cruciality/dead-code phases:
	self.is_critical = False;













