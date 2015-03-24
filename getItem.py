#!/usr/bin/env python
# -*- coding;utf-8 -*-
import re
f = open("tmp","r")
init = 0
for line in f:
	linelen = len(line)
	while True:
		start = line.find('{', init)
		if start == -1:	
			break
		end = line.find('}',start + 1)
		print line[start: end+1]
		init = end + 1
		if(init >= linelen):
			break
