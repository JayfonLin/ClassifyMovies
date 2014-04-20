#-*- coding:utf-8 -*-
import os
import operator

ff = ['action','ancient-costume','animation','biography','comedy','drama','horror','romance','sci-fi']
path = "tokens//"


count = 0
for name in ff:
    vocabulary = {}
    list_file = os.listdir(path+name+'//')
    #docNum = len(list_file)
    for f in list_file:
        #print f
        mfile = open(path+name+'//'+f, 'r')
        content = mfile.read()
        words = content.split('\n')
        words = set(words)
        for w in words:
            #print w.decode('utf-8')
            if w in vocabulary:
                vocabulary[w] = str(int(vocabulary[w])+1)
            else:
                vocabulary[w] = 1
        #for key in vocabulary.keys():
            
            #print key.decode('utf-8'), vocabulary[key]
        count += 1
        print name, ' file ', count

    vfile = open('vocabulary/'+name+'.txt', 'w+')
    vocabulary = sorted(vocabulary.items(), key=lambda d:int(d[1]), reverse=True)
    print 'length: ', len(vocabulary)
    for item in vocabulary:
        #if int(item[1]) > 0:
        vfile.write(str(item[0])+'$'+str(item[1])+'\n')
    vfile.close()
print 'finish'
    
