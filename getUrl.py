#!/usr/bin/env python
f = open("tmp","r")
for line in f:
	line = line.replace('"','').strip()
	print line
f.close();
