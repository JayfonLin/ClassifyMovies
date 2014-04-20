#-*- coding:utf-8 -*-
import Classify
import os
test=Classify.Classify()
classList = ['action','ancient-costume','animation','biography','comedy','drama','horror','romance','sci-fi']
for cl in classList:
    list_file = os.listdir('tokens/'+cl+'//')
    for lf in list_file:
        test.classfy('tokens/'+cl+'/'+lf)
