# -*- coding: cp936 -*-
import threading
import urllib
import Globalvar

g_mutex = threading.Lock()
g_pages = []      #�߳�����ҳ��󣬽�ҳ��������ӵ����list��
g_dledUrl = []    #�������ع���url
g_failedUrl = []  #����ʧ�ܵ�url
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
                g_totalcount += 1    #����ѭ��������ҳ������1
                self.download(Globalvar.g_toDlUrl[i+j])
                print 'Thread started:',i+j,'--Number = ',g_totalcount
                j += 1
            i += j
            for th in self.threadPool:
                
                print 'thread end'
                th.join(30)     #�ȴ��߳̽�����30�볬ʱ
	    print 'after join'
 	    self.updateNames()
            self.threadPool = []    #����̳߳�
        #Globalvar.g_toDlUrl = []    #����б�

    def updateNames(self):
        global g_dledUrl
	global g_pages
        newNameList = []
        for s in g_pages:
            newNameList += self.getNames(s)
	#warning
	g_pages = []   
        #g_toDlUrl = list(set(newUrlList) - set(g_dledUrl))    #��ʾunhashable
	#warning
	Globalvar.names += list(set(newNameList) - set(Globalvar.names))
                
    def Craw(self):  
            self.downloadAll()
         
class CrawlerThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url    #���߳����ص�url

    def run(self):    #�̹߳���-->����htmlҳ��
        global g_mutex
        global g_failedUrl
        global g_dledUrl
	global g_pages
        try:
            f = urllib.urlopen(self.url)
            s = f.read()
	    f.close()
	    
        except:
            g_mutex.acquire()    #�߳���-->����
            g_dledUrl.append(self.url)
            g_failedUrl.append(self.url)
            g_mutex.release()    #�߳���-->�ͷ�
            print 'Failed downloading and saving',self.url
            return None    #���ŷ���!
        
        g_mutex.acquire()    #�߳���-->����
        g_pages.append(s)
        g_dledUrl.append(self.url)
        g_mutex.release()    #�߳���-->�ͷ�
