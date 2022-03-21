
default:

gen/list.mk:
	find gen -name '*.txt' | sort -V | sed 's/^/outs += /;s/.txt$$/.png/' > $@

include gen/list.mk

all: $(outs)

gimp-%.png: gen/%.png
	gimp $<

gen/%.png: gen/%.txt
	dot -Tpng < $< > $@


