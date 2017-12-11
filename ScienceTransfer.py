# -*- coding:utf-8 -*-
import urllib2
import urllib
import BeautifulSoup
import string
import re
import xlwt
import sys
import math
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

## 爬取http://www.nstad.cn/ 上的科技成果转化库中的项目

class Item:

    def __init__(self,pid = "pid",cgmc="cgmc",school= "school",time ="time"):
        self.pid = pid
        self.cgmc =cgmc
        self.school=school
        self.time=time

url = "http://www.nstad.cn/ashx/SearchList.ashx"

head= {}
head['User-Agent']='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
xlsfile = xlwt.Workbook(encoding='utf-8')

#C 制造业 G信息传输，计算机服务和软件业 M科学研究技术服务和地质勘查业
worksheet = xlsfile.add_sheet("制科学研究技术服务和地质勘查业")
worksheet.write(0, 0, '编号')
worksheet.write(0, 1, 'pid')
worksheet.write(0, 2, '成果名称')
worksheet.write(0, 3, '完成单位')
worksheet.write(0, 4, '更新时间')

postdata = "pageIndex=1&pageSize=10&cgly=&hy='M'&cgDQ=&year="
req = urllib2.Request(url, postdata, headers=head)

html = urllib2.urlopen(req)
page = html.read()
index1 = page.find('t_red')# class t_red 现实总共多少条
index2 = page.find("/span")
numberoftext = int(page[(index1+7):(index2-1)])

numberofpage = int(math.ceil(numberoftext/20.0)) #计算page
for j in range(0,numberofpage):#遍历链接页面 从
    postDict = {
        'pageIndex': j,
        'pageSize': 20,
        'hy':"\'M'"
    };


    postdata = urllib.urlencode(postDict,1)
    req = urllib2.Request(url, postdata, headers=head)
    html = urllib2.urlopen(req)
    page = html.read()
    texts = re.findall(r'\{(.*?)\}',page)
    leng = len(texts)

    items = []
    for text in texts:
        temp = Item()
        temp.pid = re.findall(r'\d{4,8}',text)[0]

        cgmcindex = text.find('cgmc')
        cgdyindex = text.find('cgdywcdw')
        lxtimeindex = text.find('lxtime')
        temp.cgmc = text[cgmcindex + 6:cgdyindex - 2]
        temp.school = text[cgdyindex + 10:lxtimeindex - 2]

        leng = len(text)
        temp.time = text[lxtimeindex + 8:leng - 1]
        items.append(temp)


    lengofitem = len(items)
    for i in range(1, lengofitem+1):
        item = items[i-1]
        worksheet.write(i+j*20, 0, i+j*20)
        worksheet.write(i+j*20, 1, item.pid)
        worksheet.write(i+j*20, 2, item.cgmc)
        worksheet.write(i+j*20, 3, item.school)
        worksheet.write(i+j*20, 4, item.time)


print(j)

xlsfile.save('科技成果转化项目库-科学研究技术服务和地质勘查业.xls')