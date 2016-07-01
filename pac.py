#! /usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import re

def getHtml(url)
	a = urllib.urlopen(url)
	b = a.read()
	return b

def getImg(b)
	reg = r'src="(.+?\.jpg)" pic_ext'
	c = reg.compile(reg)
	d = c.findall(c,b)
	x = 0
	for imgurl in d
		urllib.urlretrieve(imgurl,'%s.jpg' %x)
		x+=1

b = getHtml("www.baidu.com")

print getImg(b)