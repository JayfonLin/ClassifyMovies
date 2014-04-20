#-*- coding:utf-8 -*-
import os
import jieba
import math
class Classify:
    def getVoCount(self):#计算vocabulary各个词的出现个数，并保存在vocount
            classList = ['action','ancient-costume','animation','biography','comedy','drama','horror','romance','sci-fi']
            voc=open('vocabularies.txt')
            con=open('voCount.txt', 'w+')
            alltokens=[]
            for cl in classList:
                list_file = os.listdir('tokens/'+cl+'//')
                st = []
                for lf in list_file:
                    lfo=open('tokens/'+cl+'/'+lf)
                    tmp=lfo.readlines()
                    for t in tmp:
                        t=t.strip('\n')
                        st.append(t)
                alltokens.append(st)
            result=[]
            amount=[0,0,0,0,0,0,0,0,0]#各列出现的总次数
            task=0
            wcount=0
            vot=voc.readlines()
            for vo in vot:
                vo=vo.strip('\n')
                countList=[]
                tokenCount=0
                for s in alltokens:
                    count=0
                    for k in s:
                        if vo==k:
                            count+=1
                    countList.append(count)
                    amount[tokenCount]+=count
                    tokenCount+=1
                wstr=''
                for co in range(1,9):
                   wstr=wstr+'$'+str(countList[co])
                wstr=str(countList[0])+wstr    
                con.write(wstr+'\n')
                task+=1
                print task
                result.append(countList)
            return amount         

    def calu(self,amount):#计算条件概率，保存在pro
        #amount=[84834, 22310, 81054, 49031, 70362, 65286, 49221, 94099, 62564]#各列的总数
        keyContent=open('vocabularies.txt')
        keyCount=open('voCount.txt')
        keyPro=open('pro.txt','w+')
        allkc=[]
        keycontentlist=keyContent.readlines()
        klen=len(keycontentlist)
        for kcount in keyCount.readlines():
            newkc=[]
            nekcount=kcount.strip('\n')
            newkc=nekcount.split('$')
            allkc.append(newkc)
        keymark=0
        allPro=[]
        for vo in keycontentlist:       
            thisPro=[]
            amountMark=0
            for alk in allkc[keymark]:              
                alkc=float(alk)
                tmpPro=math.log10(float(alkc+1)/float(klen+amount[amountMark]))
                amountMark+=1
                thisPro.append(tmpPro)
            #print thisPro
            allPro.append(thisPro)
            thisProStr=''
            for tp in thisPro:
                thisProStr=thisProStr+str(tp)+'$'
            keyPro.write(vo.strip('\n')+' '+thisProStr+'\n')             
            keymark+=1
    def ini(self):
        classList = ['action','ancient-costume','animation','biography','comedy','drama','horror','romance','sci-fi']
        self.classAmount=[1486, 30, 184, 107, 1715, 2842, 703, 1045, 415]
        self.mysum = 0
        for c in self.classAmount:
            self.mysum += c
        voc=open('pro.txt','r')
        newvoc=open('vocabularies.txt','r')
        
        voList=[]
        self.proList=[]
        voc_lines = voc.readlines()
        self.lines2 = newvoc.readlines()
        for vocr in voc_lines:#从pro文件中获得条件概率（prolist），volist为多余
            vocr=vocr.strip('\n')
            tmpVocr=vocr.split(' ')
            voList.append(tmpVocr[0])
            tmpProList=tmpVocr[1].split('$')
            del tmpProList[9]
            self.proList.append(tmpProList)
        ll = []
        for l in self.lines2:
            ll.append(l.decode('utf-8').strip('\n'))
        self.lines2 = ll
        #jieba.cut('中文')
        #print 'initialize end'
    def classfy(self,doc):#分类器，参数为文本路径，应为分好词后的文件
        classList = ['action','ancient-costume','animation','biography','comedy','drama','horror','romance','sci-fi']
        
        maxMark1=0#标记前两个最好的结果
        maxPro1=0
        maxMark2=0
        maxPro2=0
        result=[]#结果集,为各类的估计值
        matchList=[]
        #to=open(tok,'r')
        lines1=jieba.cut(doc)
        #lines1 = to.readlines()
        
        for t in lines1:#获得待分类文本在vocabulary里面的匹配情况，保存下标
            #t=t.strip('\n')
            mark=0            
            for v in self.lines2:
                #print v, t
                if v==t:
                    #print v
                    matchList.append(mark)
                mark+=1
        for i in range(0,9):#计算各类的条件概率
            thisClassPro=1
            for ma in matchList:
                thisClassPro+=float(self.proList[ma][i])#条件概率连乘
            thisClassPro+=math.log10((float(self.classAmount[i])/float(self.mysum)))#加上先验概率
            result.append(thisClassPro)
            if i==0:#保存最好的前两个分类
                maxPro1=thisClassPro
            if i==1:
                if maxPro1>thisClassPro:
                    maxPro2=thisClassPro
                    maxMark2=1
            if thisClassPro>maxPro1:
                maxMark2=maxMark1
                maxPro2=maxPro1
                maxMark1=i
                maxPro1=thisClassPro
                continue
            if thisClassPro>maxPro2:
                maxMark2=i
                maxPro2=thisClassPro
        marks = [maxMark1, maxMark2]
        return marks
        #print tok
        #print classList[maxMark1]+" "+classList[maxMark2]
        #print result  
         

