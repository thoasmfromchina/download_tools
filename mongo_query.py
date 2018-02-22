#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pymongo import MongoClient as mongoclient
import re
import time
dbuser = 
dbpass =
dbhost = 
dbport = 
database = 
collections = 

def mongo_query(search_contents):

    try:
            client = mongoclient(dbhost, dbport)
            authen_status = client.PornHub.authenticate(dbuser,dbpass)
            if authen_status is True:
                db = client[database]
                coll = db[collections]
                datas = coll.find({'video_title':re.compile(search_contents)})
                count = 0
                check_results  = []
                for data in datas:
                   count += 1
                   time.sleep(0.0001)
                   if int(data['video_duration']) > 3600:
                     tem = {}
                     tem[u'video_title'] = data['video_title'].encode("utf-8")
                     tem['video_durtion'] = int(data['video_duration'])
                     tem['video_viewkey'] = data['viewkey']
                     tem['image_url'] = data['image_url']
                     check_results.append(tem)
                return check_results
            else:
                print "Authentication failed"
    except:
            print "Error"





