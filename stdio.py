
import sys;

stderr = sys.stderr;

def printf(fmt, *args):
	print(fmt % args, end = '');

def fprintf(stream, fmt, *args):
	print(fmt % args, file = stream, end = '');

def puts(string):
	printf("%s\n", string);
	
def fputs(string, stream):
	fprintf(stream, "%s\n", string);
