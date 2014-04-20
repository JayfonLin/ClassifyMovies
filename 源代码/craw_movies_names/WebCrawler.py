# -*- coding: cp936 -*-
import threading
import urllib
import Globalvar

g_mutex = threading.Lock()
g_pages = []      #线程下载页面后，将页面内容添加到这个list中
g_dledUrl = []    #所有下载过的url
g_failedUrl = []  #下载失败的url
g_totalcount = 0

class WebCrawler:
    def getNames(self, strPage):
	counter = 0
        newNames = []
        title = strPage.find(r'alt="')
	end = strPage.find(r'"', title+5)
	abStr = strPage[title+5:end]
	while title != -1 and end != -1:
		if strPage[title+5:end] != abStr:
			newNames.append(strPage[title+5:end])
			print counter, ' ', strPage[title+5:end].decode('GBK').encode('utf-8')
		title = strPage.find(r'alt="', end+1)
		end = strPage.find(r'"', title+5)
		counter = counter + 1
        return newNames

    def __init__(self,threadNumber):
        self.threadNumber = threadNumber
        self.threadPool = []

    def download(self, url):
        Cth = CrawlerThread(url)
	Cth.setDaemon(True)
        self.threadPool.append(Cth)
        Cth.start()

    def downloadAll(self):
        global g_totalcount
        i = 0
        while i < len(Globalvar.g_toDlUrl) and not Globalvar.is_exit:
            j = 0
            while j < self.threadNumber and i + j < len(Globalvar.g_toDlUrl) and not Globalvar.is_exit:
                g_totalcount += 1    #进入循环则下载页面数加1
                self.download(Globalvar.g_toDlUrl[i+j])
                print 'Thread started:',i+j,'--Number = ',g_totalcount
                j += 1
            i += j
            for th in self.threadPool:
                
                print 'thread end'
                th.join(30)     #等待线程结束，30秒超时
	    print 'after join'
 	    self.updateNames()
            self.threadPool = []    #清空线程池
        #Globalvar.g_toDlUrl = []    #清空列表

    def updateNames(self):
        global g_dledUrl
	global g_pages
        newNameList = []
        for s in g_pages:
            newNameList += self.getNames(s)
	#warning
	g_pages = []   
        #g_toDlUrl = list(set(newUrlList) - set(g_dledUrl))    #提示unhashable
	#warning
	Globalvar.names += list(set(newNameList) - set(Globalvar.names))
                
    def Craw(self):  
            self.downloadAll()
         
class CrawlerThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url    #本线程下载的url

    def run(self):    #线程工作-->下载html页面
        global g_mutex
        global g_failedUrl
        global g_dledUrl
	global g_pages
        try:
            f = urllib.urlopen(self.url)
            s = f.read()
	    f.close()
	    
        except:
            g_mutex.acquire()    #线程锁-->锁上
            g_dledUrl.append(self.url)
            g_failedUrl.append(self.url)
            g_mutex.release()    #线程锁-->释放
            print 'Failed downloading and saving',self.url
            return None    #记着返回!
        
        g_mutex.acquire()    #线程锁-->锁上
        g_pages.append(s)
        g_dledUrl.append(self.url)
        g_mutex.release()    #线程锁-->释放
