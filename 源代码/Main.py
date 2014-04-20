#-*- coding:utf-8 -*-

from __future__ import division
import Classify
import jieba
import urllib
import urllib2
import random
import os
polyseme = u'多义词'
polyseme = polyseme.encode('utf-8')
mo = u'电影'
mo = mo.encode('utf-8')
story = u'剧情'
story = story.encode('utf-8')
director = u'导演'
director = director.encode('utf-8')
if __name__ == "__main__":
        keyfile_names = ['action','ancient-costume','animation','biography','comedy','drama','horror','romance','sci-fi']
        keys = []
        chinese = ['动作片', '古装','动画','传记','喜剧','剧情片','惊悚片','爱情片','科幻片']
        url = 'http://baike.baidu.com/searchword/'
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        
        headers = { 'User-Agent' : user_agent }
        cla = Classify.Classify()
        cla.ini()
        while 1:       
                movieName = str(raw_input('输入一个电影名（输入0退出）： '.decode('utf-8').encode('gbk')))
                if movieName == '0':
                        print '退出...'.decode('utf-8').encode('gbk')
                        break
                print "正在分析...".decode('utf-8').encode('gbk')
                values = {'word' : movieName, 'pic' : '1', 'sug' : '1', 'enc' : 'gbk'}
                data = urllib.urlencode(values)
                data=data.encode('GB2312')
                req = urllib2.Request(url, data, headers)
                response = urllib2.urlopen(req)
                if response.getcode() != 200:
                        print '查询出错'.decode('utf-8').encode('gbk')
                        continue
                s = response.read()
                
                r_url = response.geturl()
                response.close()
                
                if r_url.find('none') != -1:
                    
                    print '没找到电影'.decode('utf-8').encode('gbk')
                    continue
                #print s
                if s.find(polyseme) != -1 and s.find(story) == -1:
                    print '多义词'.decode('utf-8').encode('gbk')
                    continue
                type_movie = cla.classfy(s)
                print movieName
                print '类型 '.decode('utf-8').encode('gbk'), chinese[type_movie[0]].decode('utf-8').encode('gbk'), ' ', chinese[type_movie[1]].decode('utf-8').encode('gbk')
