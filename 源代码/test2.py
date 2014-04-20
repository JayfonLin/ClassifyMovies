#encoding=utf-8
import jieba
#f = open('1.html')
f = open('2.txt')
content = f.read()
seg_list = jieba.cut(content)
#seg_list = jieba.cut(u'asdf中文【】,,. ~    \n\t\ssdf', cut_all=False)
#print " / ".join(seg_list)  # 精确模式
for s in seg_list:
    print s
#seg_list = jieba.cut_for_search(content)  # 搜索引擎模式
#print ", ".join(seg_list)
