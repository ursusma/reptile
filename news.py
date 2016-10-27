#!/usr/bin python
# -*- coding:utf-8 -*-

import re
import urllib.request
import requests
import string

def geturl(url):
    a = urllib.request.Request(url)
    a.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36' '(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')
    dateurl = urllib.request.urlopen(url).read().decode('gbk')
    return dateurl

def reurl(dateurl):
    title_re = re.compile(r'title":"(.*)",\W+.*\W+.*:"(.*)"')
    tetol = re.findall(title_re,dateurl)
    return tetol

def getdate(tetol):
    text = []
    for i in tetol:
        newsurl = i[1]
        b = urllib.request.urlopen(newsurl)
        bt = b.read().decode('gbk')
        text_re = re.compile(r'<p>(.*?)</p>')
        text.append(re.findall(text_re,bt))
        b.close()
    return text

def handlestr(tetol,text):
    k = 0
    st = ''
    for test in text:
        title = tetol[k][0]
        test = text[k]
        x = ''
        for o in test:
            if o == u'用微信扫码二维码' or o == '分享至好友和朋友圈':
                pass
            else:
                x += '    ' + o + '\n'
                req = re.compile(r'<.*?>')
                test = req.sub('',x)
        k += 1
        number = str(k)
        st += number + '.' + title + '\n' + x +'\n\n'
    return st

def writetext(st):
	f = open('news.doc','w')
	f.write(st)
	f.close

url = "http://temp.163.com/special/00804KVA/cm_yaowen.js?callback=data_callback"
dateurl = geturl(url)
tetol = reurl(dateurl)
text = getdate(tetol)
st = handlestr(tetol,text)
writetext(st)

'''c = v1 + /n +'''