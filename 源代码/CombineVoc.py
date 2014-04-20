#-*- coding:utf-8 -*-
import os
voc = []
list_file = os.listdir('feature selection//')
for l in list_file:
    f = open('feature selection/'+l,'r')

    lines = f.readlines()
    voc += list(set(lines)-set(voc))
    f.close()
outf = open('vocabularies.txt','w+')
for v in voc:
    outf.write(v)
outf.close()
print 'length: ', len(voc)
print 'end'
    
