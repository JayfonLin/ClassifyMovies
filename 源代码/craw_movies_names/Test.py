#-*- coding:utf-8 -*-
import WebCrawler
import signal
import Globalvar

def handler(signum, frame):
     Globalvar.is_exit = True
     print "receive a signal %d, is_exit = %d"%(signum, Globalvar.is_exit)

if __name__ == "__main__":
	signal.signal(signal.SIGINT, handler)
	signal.signal(signal.SIGTERM, handler)
	s =  '�������url(��-->http://www.baidu.com): \n'
	url = raw_input('�������url(��-->http://www.baidu.com): \n'.decode('GBK').encode('utf-8'))
	thNumber = int(raw_input('�����߳���:'.decode('GBK').encode('utf-8')))    #֮ǰ����δת����bug

	wc = WebCrawler.WebCrawler(thNumber)
	wc.Craw(url)

	while 1:
	    alive = False
	    for th in wc.threadPool:
		alive = alive or th.isAlive()
	    if not alive:
		print 'break'
		break 
