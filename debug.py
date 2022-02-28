
depth = 0;

def indent():
	global depth;
	depth += 1;

def unindent():
	global depth;
	depth -= 1;

def dprint(string):
	global depth;
	print(" " * depth + string);

def dpv():
	assert(not "TODO");

