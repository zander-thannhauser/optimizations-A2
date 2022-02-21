
# expression_table will be modified

def Block_optimize(this):
	# initial references to a global register should use what's in block.needs
	
	# for each i2i but the last:
		# change to movi, change references until next i2i
	# the last i2i to write the block.provides
		# any references afterward to refer to block.provides
	
	# same sorta thing for stores and loads, but the behavour needs to reset
		# bewteen {,i,f}call instructions
	
	# preform A1 optimizations...
	
	# that last instructions might have changed,
		# update this.children accordingly.
	
	assert(not "TODO");
	

