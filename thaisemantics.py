#! /usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2, json

words = u'หมู่เรือปราบปรามโจรสลัด ฝึกใหญ่เตรียมความพร้อม ก่อนออกปฏิบัติงานร่วมกับกองกำลังผสมทางเรือนานาชาติ ที่อ่าวเอเดนและชายฝั่งโซมาเลีย ในวันที่ 12 กรกฎาคม นี้'
request = { 
           'api_key': '547bce78d5568489b44484cc6a9fca49587a45de24d21718175823ad4027e87b',
           'method': 'SWATH',
           'params': [words]
        }
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "application/json"}        
params = json.dumps(request)
# print params
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "application/json"}
url = 'https://www.thaisemantics.org/service/rest/'
req = urllib2.Request(url, params)
req.add_header('Content-type','application/x-www-form-urlencoded')
req.add_header('Accept','application/json')
u = urllib2.urlopen(req)
data = u.read()
json_data = json.loads(data)
for sep_data in json_data['result']:
	print sep_data