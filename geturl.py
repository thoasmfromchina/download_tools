#!/usr/bin/env python
#-*- coding:utf-8 -*-
import requests,os,time
url = "http://127.0.0.1:10090/api/v0.1/pornhub_query"
datas = requests.get(url).json()
urls = []
count = 0
for data in datas:
    count += 1
    url = data['image_url']
    r = requests.get(url,stream=True)
    try:
            f = open("/tmp/pic/"+str(data['video_title'].encode('UTF-8'))+".jpg","wb")
            for chunk in r.iter_content(chunk_size=512):
              if chunk:
                f.write(chunk)
                print "Downloading "+url
    except:
            time.sleep(10)
            pass
