#! /usr/bin/env python
# -*- coding: utf-8 -*-

import thaisemantics, sys, time, os, codecs

def wordcut(msg):
	start_time = time.time()
	f = codecs.open('in.txt','w', 'utf-8')
	f.write(u'ตรวจสอบ'.encode('utf-8'))
	f.close()
	print(os.popen('wordcut <in.txt> out.txt').readline())
	#x = _
	#print(x)
#	command = os.popen('wordcut <in.txt> out.txt').readline()
#	print command
	print time.time()-start_time, "second"


arg = sys.argv[1]
#print arg

#wordcut('test')
swath(arg)
