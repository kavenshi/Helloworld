# -*-coding:utf-8-*-
import urllib.request
import re
import time
import urllib.error



def use_proxy(proxy_addr,url):
    try:
        import urllib.request
        proxy = urllib.request.ProxyHandler({'http':proxy_addr})
        opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        data = urllib.request.urlopen(url).read().decode('utf-8')
        return data
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        time.sleep(10)
    except Exception as e:
        print("exception:"+str(e))
        time.sleep(1)


def getlisturlwithproxy(key,pagestart,pageend,proxy):
    try:
        page=pagestart
        keycode=urllib.request.quote(key)
        pagecode = urllib.request.quote("&page")
        for page in range(pagestart,pageend+1):
            #http://weixin.sogou.com/weixin?type=2&query=%E7%BD%91%E5%AE%BF%E7%A7%91%E6%8A%80&ie=utf8&s_from=input&_sug_=y&_sug_type_=&w=01019900&sut=5384&sst0=1505019956418&lkt=1%2C1505019956315%2C1505019956315
            url="http://weixin.sougou.com/weixin?type=2&query="+keycode+pagecode+str(page)
            data1 = use_proxy(proxy,url)
            listurlpat = '<div class="news-box">.*?(http://.*?)"'
            listurl.append(re.compile(listurlpat,re.S).findall(data1))
        print("共获取到"+str(len(listurl))+'页')
        return listurl
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
        time.sleep(10)
    except Exception as e:
        print("exception:" + str(e))
        time.sleep(1)


def getlisturl(key, pagestart, pageend):
    try:
        page = pagestart
        keycode = urllib.parse.quote(key)
        for page in range(pagestart, pageend + 1):
#http://weixin.sogou.com/weixin?query=%E7%BD%91%E5%AE%BF%E7%A7%91%E6%8A%80&_sug_type_=&sut=5384&lkt=1%2C1505019956315%2C1505019956315&s_from=input&_sug_=y&type=2&sst0=1505019956418&page=7&ie=utf8&w=01019900&dr=1
            url1 = "http://weixin.sogou.com/weixin?query=" + keycode + '&page=' + str(page)
            data = urllib.request.urlopen(url1).read().decode('utf-8')
            listurlpat = '<div class="txt-box">.*?("http://.*?)"'
            listurl.append(re.compile(listurlpat, re.S).findall(data))
            print("共获取到" + str(len(listurl)) + '页')
        return listurl
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
        time.sleep(10)
    except Exception as e:
        print("exception:"+str(e))
        time.sleep(1)

#User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36
headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
listurl = []
key = "网宿科技"
#proxy = "119.6.136.122:80"
pagestart = 1
pageend =5
listurl = getlisturl(key,pagestart,pageend)
