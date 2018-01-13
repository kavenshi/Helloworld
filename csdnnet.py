# -*-coding:utf-8-*-
import urllib.request
#User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36

# url = "https://www.itjuzi.com/person"
# file = urllib2.urlopen(url) # 403 forbidden

# header =("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
# opener = urllib2.build_opener()
# opener.addheaders = [header]
# data = opener.open(url).read()

# req = urllib2.Request(url)
# req.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
# data = urllib2.urlopen(req).read()
# print(data)

keyword= '容器'
keycode = urllib2.quote(keyword)
url = "http://www.baidu.com/s?wd="+keycode
req = urllib2.Request(url)
file = urllib2.urlopen(req)
data = file.read()
fhandle = open('2.html','wb')
fhandle.write(data)
fhandle.close()


