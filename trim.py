#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
def todelete(item):
	return len(item) >= 5

f = open("data.json","r")
for line in f:
	linelen = len(line)
	if(linelen == 2):
		continue
	for x in range(0, linelen):
		if(line[x] == '['):
			break
	for y in range(linelen - 1, -1, -1):
		if(line[y] == ']'):
			break;
	parsedLine = line[x+1:]
	#print parsedLine
	#print parsedLine

#	itemArray = re.split('[{}]', parsedLine)
	itemArray = parsedLine.split(',')
	itemArrayLen = len(itemArray)
	print itemArray[0]
	filteredItemArray = filter(todelete,itemArray) 
	itemArrayLen = len(filteredItemArray)
	#for x in range(0, itemArrayLen):
	#	print filteredItemArray[x]
f.close()
