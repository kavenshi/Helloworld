# -*- coding:utf-8 -*-
# 爬取深交所 上市公司的减持公告

import urllib2
import re
from bs4 import BeautifulSoup
import string
import sys
import xlwt
import urllib
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

# 爬取深交所减持公告 每个月进行
url = "http://disclosure.szse.cn/m/search0425.jsp"

head={}
head['User-Agent']='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'

postdata= 'leftid=1&lmid=drgg&pageNo=1&stockCode=&keyword=%BC%F5%B3%D6&noticeType=&startTime=2017-12-08&endTime=2017-12-08&imageField.x=45&imageField.y=14&tzy='
starttime = '2017-12-08'
endtime = '2017-12-08'
keyword="减持"
dict = {"keyword":keyword,"startTime":starttime,"endTime":"endtime"}
postdata1 = urllib.urlencode(dict)

utf8kw = urllib2.quote(keyword)


html = urllib2.urlopen(url)
req=urllib2.Request(url,postdata,headers=head)
html= urllib2.urlopen(req)
content = html.read()

print(content)
soup = BeautifulSoup(content,'html.parser')
#print(soup.prettify())

# 记入到xls文件中
xlsfile = xlwt.Workbook(encoding='utf-8')
worksheet = xlsfile.add_sheet("减持公告")
worksheet.write(0, 0, '编号')
worksheet.write(0, 1,'公告名')
worksheet.write(0, 2, '链接')
worksheet.write(0,3,'日期')


#items = soup.find_all('a',target="new")
items=soup.find_all("td",align="left",class_="td2")
i=1;
for item in items:
    text = item.text
    href = "http://disclosure.szse.cn/"+item.contents[0].get('href')
    date = item.contents[5].string
    worksheet.write(i,0,i)
    worksheet.write(i, 1, text)
    worksheet.write(i, 2, href)
    worksheet.write(i,3,date)
    i=i+1


xlsfile.save('减持公告.xls')





