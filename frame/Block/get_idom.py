
from stdio import printf;

def Block_get_idom(self, stopat = set([])):
	# print("self.parents == %s" % str([str(p) for p in self.parents]));
	assert(not "TODO");
#	if not self.idom and len(self.parents) > 0:
#		print(f"self = \"{self.label}\" ({id(self)})");
#		parents = [p for p in self.parents if p is not self];
#		if len(parents) == 1:
#			self.idom = parents[0];
#		else:
#			index = 0;
#			paths = [[p] for p in parents]
#			while len(paths) > 1:
#				for i, p in enumerate(paths):
#					printf("%2s [%i] = %s\n", \
#						"->" if i == index else "", i, \
#						str([f"{b.label} ({id(b)})" for b in p]));
#				
#				path = paths[index];
#				head = path[-1];
#				if head not in stopat:
#					newstopat = stopat.copy();
#					newstopat.add(self);
#					next = head.get_idom(newstopat);
#					if next:
#						print(f"next == \"{next.label}\" ({id(next)})");
#						if any(next in p for p in paths):
#							self.idom = next;
#							printf("path [%i] merged.\n", index);
#							paths.pop(index);
#						else:
#							path.append(next);
#				
#				index += 1;
#				if index >= len(paths):
#					index = 0;
#			
#			for i, p in enumerate(paths):
#				printf("%2s [%i] = %s\n", \
#					"->" if i == index else "", i, \
#					str([f"{b.label} ({id(b)})" for b in p]));
#		if self.idom:
#			print(f"return \"{self.idom.label}\" ({id(self.idom)});");
#		else:
#			print("return None;");
#	
	return self.idom;











