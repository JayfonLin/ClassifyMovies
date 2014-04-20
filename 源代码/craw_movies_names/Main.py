#-*- coding:utf-8 -*-
#Main.py
import urllib
import time
import threading
import Globalvar
import WebCrawler
import signal

ff = ['action','ancient-costume','animation','biography','comedy','drama','horror','romance','sci-fi']
def handler(signum, frame):
     Globalvar.is_exit = True
     print "receive a signal %d, is_exit = %d"%(signum, Globalvar.is_exit)

g_mutex = threading.Lock()
g_totalcount = 0  #下载过的页面数
page = 2
theme = []

if __name__ == "__main__":
	signal.signal(signal.SIGINT, handler)
	signal.signal(signal.SIGTERM, handler)
	theme = str('comedy')
	thNumber = int(raw_input(r'thread number:'))    #之前类型未转换出bug
	Globalvar.g_toDlUrl.append(str('http://www.ffdy.cc/type,genre/movie,'+theme+'/'))
	
	while page <= 121:
		Globalvar.g_toDlUrl.append(str('http://www.ffdy.cc/type,genre/movie,'+theme+'/index_'+str(page)+'.html'))
		page += 1
	print 'start craw'
	wc = WebCrawler.WebCrawler(thNumber)
	wc.Craw()

	while 1:
	    alive = False
	    print 'running'
	    for th in wc.threadPool:
                alive = alive or th.isAlive()
	    if not alive:
		print 'break'
		break 
	j = 0
	print 'write to file txt'
	content = open(r'movies/movies_'+theme+'.txt', 'w+')
	#content.write(u'电影列表')
	while j < len(Globalvar.names):
		content.write(Globalvar.names[j] + str('\n'))
		j = j + 1
	else:
                content.write('total: '+str(j))
                content.close()
		print 'finished'
	


