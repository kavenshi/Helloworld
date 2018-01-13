import re

def getcontent(listurl):
    i=0
    for i in range(0,len(listurl)):
        for j in range(0,len(listurl[i])):
            try:
                url=listurl[i][j]
                url=url.replace("amp;""")
                #open the url
                data =
                titlepat = "<title>(.*?)</title>"
                contentpat='id="js_content">(.*?)id="js_sg_bar"'
                title = re.compile(titlepat).findall(data)
                content=re.compile(contentpat).findall(data)

