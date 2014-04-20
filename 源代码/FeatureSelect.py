# -*- coding: gbk -*-

from __future__ import division
import os
ff = ['action','ancient-costume','animation','biography','comedy','drama','horror','romance','sci-fi']
path1 = "tokens//"
path2 = 'vocabulary//'
#path2 = 'vocabulary//action.txt'
    
vocabulary = []
alens = {}
count1 = 0
n = 0
for ts in ff:
    list_file = os.listdir(path1+ts+'//')
    #alens.append(len(list_file))
    alens[ts]=len(list_file)
    n += len(list_file)
    d = dict()
    vfile = open(path2+ts+'.txt')
    content = vfile.read()
    vfile.close()
    lines = content.split('\n')

    for line in lines:
        #print line.split('$')[0].decode('utf-8'), ' ', line.split('$')[1]
        a = line.split('$')
        if len(a) > 1:
            d[a[0]] = a[1]
        #print 'line finish'
    vocabulary.append(d)
    count1 += 1
count1 = 0
print 'state1 finish'

while count1 < 9:
    v = vocabulary[count1]
    v_len = len(v)
    n11 = [0]*v_len
    n10 = [0]*v_len
    n01 = [0]*v_len
    n00 = [0]*v_len
    x2s = []
    count2 = 0
    for key in v.keys():
        count3 = 0
        for vv in vocabulary:
            if count1 == count3:
                n11[count2] = int(vv[key])
                n01[count2] = (int(alens[ff[count3]])-n11[count2])
            else:
                if vv.get(key, 'N/A') != 'N/A':
                    n10[count2] += int(vv[key])
                    n00[count2] += (int(alens[ff[count3]])-int(vv[key]))
                else:
                    n00[count2] += (int(alens[ff[count3]]))
            count3 += 1
        #print key.decode('utf-8'), ' ', n11[count2],' ', n10[count2], ' ', n01[count2], ' ', n00[count2]
        div = ((n11[count2]+n01[count2])*(n11[count2]+n10[count2])*(n10[count2]+n00[count2])*(n01[count2]+n00[count2]))
        if div == 0:
            mx2 = 0
        else:
            mx2 = n*(n11[count2]*n00[count2]-n10[count2]*n01[count2])*(n11[count2]*n00[count2]-n10[count2]*n01[count2])/div
        a = [key, mx2]
        x2s.append(a)
        count2 += 1
    x2s.sort(key=lambda x:x[1],reverse=True)
    fea_file = open('feature selection//'+ff[count1]+'.fs', 'w+')
    count4 = 0
    for x in x2s:
        if count4 < 200:
            #print x
            fea_file.write(str(x[0])+'\n')
        count4 += 1
    count1 += 1
    print 'part finish'
    
print 'finish'
    

            
        

        
    
