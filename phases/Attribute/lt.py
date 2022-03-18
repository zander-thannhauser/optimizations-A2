
def AttributePhase_lt(self, other):
	return False \
		or self.kind < other.kind \
		or self.block.rank < other.block.rank;


