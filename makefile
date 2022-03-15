
default:

gen/list.mk:
	find gen -name '*.txt' | sed 's/^/outs += /;s/.txt$$/.png/' > $@

include gen/list.mk

all: $(outs)

gen/%.png: gen/%.txt
	dot -Tpng < $< > $@


