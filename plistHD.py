# -*- coding: utf-8 -*-
import os, time, urllib

t =	 	'*****************************************************'
x = 	'* (C) 2015 - 2018 Aleksey S.Galickiy for ProxyTV.RU *'
t = 	'*****************************************************'

uAu = '"https://www.youtube.com/channel/UCQGGNWAIMrlmfMZN-oO3fPQ"'

def openSet():
	plist = ''
	kodi  = ''
	try:
		openSet = open('set.txt', 'r')
		for line in openSet.readlines():
			if line.find("kodi") != -1: 
				kodi = line.rstrip('\t\r\n')		
			elif line.find("m3u") != -1: 
				plist = line.rstrip('\t\r\n')	
		openSet.close()
	except:
		pass
	return plist, kodi
	
def newPlistHD(plist):
	extInf = '#EXTINF'
	line2 = False
	try:
		if plist.find("http") != -1:
			con = urllib.urlopen(plist)
		else:
			con = open(plist)
		openNewList = open('plistHD.m3u', 'w')
		openNewList.write('#EXTM3U url-autor="%s"\n\n' % uAu)
		for line in con.readlines():
			if line2:
				openNewList.write(line)
				line2 = False
			if line.find(extInf) != -1 and (line.find("HD") != -1 or line.find("4K") != -1):
				openNewList.write(line)
				line2 = True
		openNewList.close()
		con.close()
		print "OK. File created plistHD.m3u"
	except:
		print "No connect or file not found"

def start():
	print '%s\n%s\n%s\n\n' % (t, x, t)
	plist, kodi = openSet()
	if plist != '': 
		newPlistHD(plist)
		if kodi  != '': os.startfile(kodi)
	else: 
		print "Path file m3u not found"
	time.sleep(2)
	
start()