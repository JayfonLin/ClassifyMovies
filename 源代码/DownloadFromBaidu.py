#coding='utf-8'
import urllib.parse
import urllib.request
import time

url = 'http://baike.baidu.com/searchword/?'
verify = "http://verify.baidu.com"

file = open('movies.txt','r')

i = 1

while i != 5000:
    line = file.readline()
    i = i+1

number = 5000

proxy_number = 0

line = file.readline()

while line :
    try :
        
        dot = '.'

        ndot = line.index(dot)

        ind = ndot + 2

        line = line[ind:].strip()

        if line.rfind('/')!=-1:
            while line.rfind('/')!=-1:
                line.rstrip('/')
            
        else :
            if line.rfind('?')!=-1:
                while line.rfind('?')!=-1:
                    line.rstrip('?')
                
            else :

                proxies = ['111.1.36.26:80','202.106.16.36:3128','221.181.192.23:80','120.198.230.62:84','183.129.198.254:80','60.194.150.122:80'] 

                proxy_index = 3
                
                proxy = proxies[proxy_index]
                
                proxy_support = urllib.request.ProxyHandler({'http':proxy})

                opener = urllib.request.build_opener(proxy_support)

                urllib.request.install_opener(opener)

                index = number % 9
                
                values = {'word' : line, 'pic' : '1', 'sug' : '1', 'enc' : 'gbk'}
                
                data = urllib.parse.urlencode(values)

                data=data.encode('GB2312')

                req = urllib.request.Request(url, data)

                response = urllib.request.urlopen(req)

                if response.getcode() == 200 :

                    the_page = response.read()

                    while verify in str(the_page) :
                        
                        print ("verify occured! the proxy is " + proxy)

                        proxy = proxies[proxy_index + 1]
                
                        proxy_support = urllib.request.ProxyHandler({'http':proxy})

                        opener = urllib.request.build_opener(proxy_support)

                        urllib.request.install_opener(opener)

                        values = {'word' : line, 'pic' : '1', 'sug' : '1', 'enc' : 'gbk'}
                
                        data = urllib.parse.urlencode(values)
    
                        data=data.encode('GB2312')

                        req = urllib.request.Request(url, data)

                        response = urllib.request.urlopen(req)

                        the_page = response.read()
                    
                    filename =str( line + '.html')

                    print (str(number) + ". downloading《" + line + "》  the proxy is " + proxy )
    
                    open(filename, 'wb+').write(the_page)

                    number = number + 1

                    proxy_number = number % 50
        
                    line = file.readline()

                else :
                    print ("error")

    except :
        pass
    
else:
    print("end of file")
