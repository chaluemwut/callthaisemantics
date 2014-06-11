#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys, time, os, codecs

def wordcut():
	start_time = time.time()
	# f = codecs.open('in.txt','w', 'utf-8')
	# f.write(u'ตรวจสอบ'.encode('utf-8'))
	# f.close()
	print(os.popen('wordcut <in.txt> out.txt').readline())
	#x = _
	#print(x)
#	command = os.popen('wordcut <in.txt> out.txt').readline()
#	print command
	print time.time()-start_time, "second"

wordcut()