#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string
import urllib.request
import re

class HTML_TOOL:
    BgnChartoNoneRex = re.compile("\t|\n||<a.*?>||<img.*?>|")
    EndCharToNoneRex = re.compile("<.*?>")
    BgnParRex = re.compile("<p.*?>")
    charToNewLineRex= re.compile("(<br/>|</p>|<tr>|<div>|</div>)")
    charToNewTabRex = re.compile("<td>")
    replaceTab = [("<","<"),(">",">"),("&","&"),("&","\""),(" "," ")]

    def Replace_char(self,x):
        x= self.BgnChartoNoneRex("",x)
        x= self.BgnParRex("\n   ",x)
        x = self.CharToNewLineRex("\n",x)
        x = self.CharToNextTabRex.sub("\t", x)
        x = self.EndCharToNoneRex.sub("", x)

        for t in self.replaceTab:
            x =x.replace(t[0],t[1])
            return x

class Baidu_Spider:
    def __init__(self,url):
        self.myURL = url+'?see_lz=1'
        self.datas = [];
        self.myTool = HTML_TOOL();
        print('已经启动百度贴吧爬虫')

    def baidu_tieba(self):
        myPage = urllib.request.urlopen(self.myURL).read()
        endPage = self.page_counter(myPage)
        title = self.find_title(myPage)
        print('文章名称'+title)
        self.save_data(self.myURL,title,endPage)

    def page_counter(self,myPage):
        myMatch = re.search('<   class="red">(\d+?)</span>', myPage, re.S)
        if myMatch:
            endpage = int(myMatch.group(1))
            print('共有%d页内容'% endpage)
        else:
            endpage = 0;
            print('无法计算页数')
        return endpage

    def find_title(self,mypage):
        myMatch = re.search(r'<h1.*?>(.*?)</h1>', mypage, re.S)
        title = u'暂无标题'
        if myMatch:
            title =myMatch.group(1)
        else:
            print('无法加载标题')
        title = title.replace('\\','').replace('/','').replace(':','').replace('*','').replace('?','').replace('"','').replace('>','').replace('<','').replace('|','')
        return title

    def save_data(self,url,title,endpage):
        self.get_data(url,endpage)
        f = open(title+'.txt','w+')
        f.writelines(self.datas)
        f.close()
        print('爬虫报告：文件已下载到本地并打包成txt文件')

    def get_data(self,url,endPage):
        url = url+'&pn='
        for i in range(1,endPage+1):
            print('正在加载'%i)
            myPage= urllib.request.urlopen(url+str(i)).read()
            self.deal_data(myPage.decode('gbk'))

    def deal_data(self,myPage):
        myItem = re.findall('id = "post_content.*?>(.*?)</div>',myPage,re.S)
        for item in myItem:
            data = self.myTool.Replace_char(item.replace("\n","").encode('gbk'))
            self.datas.append(data+'\n')

# 以某小说贴吧为例子
# bdurl = 'http://tieba.baidu.com/p/2296712428?see_lz=1&pn=1'

print('请输入贴吧的地址最后的数字串：')
#bdurl = 'http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/'))
#调用
bdurl = 'https://tieba.baidu.com/f?ie=utf-8&kw='
bdurl = bdurl+urllib.parse.quote('王者荣耀')+'&fr=search'


mySpider = Baidu_Spider(bdurl)
mySpider.baidu_tieba()