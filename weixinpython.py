# -*-coding:utf-8-*-
import urllib2
import time
import urllib.error

url = 'http://weixin.sogou.com/weixin?type=2&query=物联网&ie=utf8&s_from=input&_sug_=y&_sug_type_='

headers=[];

urllib.install_opener(opener)
listurl=[]

def use_proxy(proxy_addr,url)
    try:
        import url.request
        proxy_addr