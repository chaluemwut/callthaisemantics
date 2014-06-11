#! /usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2, sys, json

# words = u'หมู่เรือปราบปรามโจรสลัด ฝึกใหญ่เตรียมความพร้อม ก่อนออกปฏิบัติงานร่วมกับกองกำลังผสมทางเรือนานาชาติ ที่อ่าวเอเดนและชายฝั่งโซมาเลีย ในวันที่ 12 กรกฎาคม นี้'

words = u'ฉันกำลังจะออกจากบ้าน'

def swath(msg):
	request = { 
	           'api_key': '547bce78d5568489b44484cc6a9fca49587a45de24d21718175823ad4027e87b',
	           'method': 'SWATH',
	           'params': [msg]
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

def orchild(msg):
	request = { 
	           'api_key': '547bce78d5568489b44484cc6a9fca49587a45de24d21718175823ad4027e87b',
	           'method': 'ORCHID',
	           'params': [msg]
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
	for sep_data in json_data['result'][0]:
		print 'word ',sep_data[0], ' type ',sep_data[1]

arg = sys.argv[1]
if arg == 'swatch':
	swath(u'"เอกนัฏ"โพสต์Instagram"สุเทพ"ออกจากห้องผ่าตัดแล้วอาการปลอดภัย')
elif arg == 'orchild':
	orchild()

