#-*- coding:utf-8 -*-
#import CDict
import jieba
import os
import re
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
#d = CDict.CDict()
ff = ['action','ancient-costume','animation','biography','comedy','drama','horror','romance','sci-fi']
path1 = "tokens//"
path2 = 'baidubaike//'
for name in ff:
    mymkdir('tokens/'+name)
    list_file = os.listdir(path2+name+'//')
    for f in list_file:
        #print f
        mfile = open(path2+name+'//'+f)
        content = mfile.read()
        #words = d.segWords(content)
        words = jieba.cut(content)
        tk = open(path1+name+'//'+f.split('.htm')[0]+'.tok', 'w+')
        for w in words:
            tk.write(w.encode('utf-8')+'\n')
print 'finish'
