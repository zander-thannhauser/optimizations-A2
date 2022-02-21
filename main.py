#!/usr/bin/env python3.10

from sys import argv;

from stdio import fprintf, stderr;

#from defines.argv0 import argv0;

from tokenizer import tokenizer;
from printer import printer;

from data import process_data;
from text import process_text;

if len(argv) < 2:
	fprintf(stderr, "%s: missing filename!\n", argv[0]);
	exit(1);

filename = argv[1];

t = tokenizer(filename);
p = printer(filename[:-3] + ".oil");

next(t);

process_data(t, p);

process_text(t, p);

if t.token != "":
	fprintf(stderr, "%s: unknown token: \"%s\"!\n", argv[0], t.token);
	exit(1);

print("exit(0)");




