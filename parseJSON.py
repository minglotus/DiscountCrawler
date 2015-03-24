#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import re
from pprint import pprint
def cmp_rate(a, b):
	if a > b:
		return -1
	elif a < b:
		return 1
	else:
		return 0
import operator
with open('data.json') as f:
	data = json.load(f)
	'''
	print "type is "
	print type(data)
	print type(data["items"])
	'''
	#print 'before', data["items"]
	data["items"].sort(cmp=cmp_rate, key=operator.itemgetter('rate'))
	#print  str(data["items"]).encode('gbk')
	datalen = len(data["items"])
	print "loadinfo(["
	for x in range(0, datalen):
		#print str(data["items"][x])
		dictlen = len(data["items"][x])
		category = data["items"][x][u'category']
		#print strdata.encode('utf-8')
		desc = data["items"][x][u'description']
		src = data["items"][x][u'source']
		url = data["items"][x][u'url']
		price = data["items"][x][u'price']
		imgsrc = data["items"][x][u'imgsrc']
		disct = data["items"][x][u'discount']
		rate = data["items"][x][u'rate']
		time = data["items"][x][u'time']
		itemid = data["items"][x][u'id']
		pubdata = data["items"][x][u'_pub_date']
		name = data["items"][x]['name']
		print "{\"category\":\"", category.encode('utf-8'), "\", \"name\": \"", name.encode('utf-8'), "\",\"discount\":\"", disct.encode('utf-8'), "\",\"url\":\"", url, "\",\"price\":\"", price.encode('utf-8'), "\" ,\"source\":\"", src.encode('utf-8'), "\",\" imgsrc\":\"", imgsrc, "\",\"description\":\"", desc.encode('utf-8'), "\" , \"rate\":\"", rate, "\"},"
	print "]);"
	        	
