# -*- coding:utf-8 -*-

import urllib2
import re
import BeautifulSoup


# 爬取深交所减持公告 每个月进行
url = "http://disclosure.szse.cn/m/search0425.jsp"

head={}
head['User-Agent'] ="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"

postdata= 'stockCode=&keyword=%BC%F5%B3%D6&noticeType=&startTime=2017-10-26&endTime=2017-12-0'
#starttime = ''
#endtime = ''

html = urllib2.urlopen(url)
req=urllib2.Request(url,postdata,headers=head)
html= urllib2.urlopen(req)
content = html.read()

soup = BeautifulSoup(content)

