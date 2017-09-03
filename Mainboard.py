# -*-coding:utf-8-*-
import urllib2
import re

def craw(url,page):
    html1 = urllib2.urlopen(url).read()
    html1=str(html1)
    pat1 = '<div id = "plist".+?<div class="page clearfix">'
    result1 = re.compile(pat1).findall(html1)
    result1 = result1[0]
    pat2 = '<img width="220" "height"="220" data-img="1" data-lazy-img="//(.+?\.jpg)">'
    imglist = re.compile(pat2).findall(result1)
    x =1
    for imagurl in imglist:
        imgname = str(page)+str(x)+".jpg"
        imagurl = "http://"+imagurl
        try:
            urllib2.urlretrieve(imagurl,filename=imgname)
        except urllib2.URLError as e:
            if hasattr(e,"code"):
                x+=1
            if hasattr(e,"reason"):
                x+=1
            x+=1


    for i in range(1,79):
        url="https://search.jd.com/Search?keyword=硬盘&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=硬盘&page="+str(i)
        craw(url,i)
        print(i)


# https://search.jd.com/Search?keyword=硬盘&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=硬盘&page=3&s=52&click=0

