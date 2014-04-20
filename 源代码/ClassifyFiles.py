#-*- coding:utf-8 -*-
import os
import shutil
def mymkdir(path):
    # 引入模块
    import os
 
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print path+' 创建成功'
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print path+' 目录已存在'
        return False
ff = ['action','ancient-costume','animation','biography','comedy','drama','horror','romance','sci-fi']
fff = 'movies_'
not_exist = u'您所进入的词条不存在'
not_exist = not_exist.encode('utf-8')
polyseme = u'多义词'
polyseme = polyseme.encode('utf-8')
s = os.getcwd()#获取当前目录  
#list_file = os.listdir(s+"\\baidubaike")
#op = OpenMovieFiles.OpenMovieFiles('.html', 'htm')
#a = op.endWith()
#f_file = filter(a,list_file)
for mf in ff:
    fff = 'movies_'+mf+'.txt'
    mymkdir('baidubaike/'+mf)
    mfiles = open('new movies/'+fff)
    #content = mfiles.read()
    lines = mfiles.readlines()
    for line in lines:
        try:
            of = open(s+'\\baidubaike\\'+line.split('\n')[0]+'.html')
        except:
            print "don't exist ", line
            continue
        ocontent = of.read()
        of.close()
        
        if ocontent.find(not_exist) != -1 or ocontent.find(polyseme) != -1:
            print 'uncorrent html, abort ', line
            continue
        try:
            shutil.copyfile(s+'\\baidubaike\\'+line.split('\n')[0]+'.html', s+'\\baidubaike\\'+mf+'\\'+line.split('\n')[0]+'.html')  
            print 'copy successfully ', line
        except:
            print line.split('\n')[0], ' copy failed'
            continue
    
    

