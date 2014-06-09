#! /usr/bin/env python
# -*- coding: utf-8 -*-

import thaisemantics, sys, time, os

def wordcut(msg):
	start_time = time.time()
	f = open('in.txt','w')
	f.write(msg)
	command = os.popen('wordcut <in.txt> out.txt').readline()
	print command
	print time.time()-start_time, "second"


arg = sys.argv[1]
print arg

wordcut('ฉันกำลังเดินออกจากบ้าน')
# swath(u'ทดสอบ')