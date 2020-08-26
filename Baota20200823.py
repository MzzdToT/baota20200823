import requests
import sys
import re

filename = sys.argv[1]

url_list=[]

f=open('result2.txt','w')


def main():
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    #扫描并输出存在漏洞的url
    for i in url_list:

        try:
            r=requests.get(i,headers=header,timeout=5)

            if re.search(r'phpmyadmin',r.text):
                print('[*] %s Is Vulnerable !' %i)
                f.write('%s\n' %i)
            else:
                print('[!] %s Is Not Vulnerable' %i)
        except Exception as e:
            print('[-] %s Is Timeout' %i)



if __name__ == '__main__':
    #获取扫描地址
    for i in open(filename):
        #处理无效字符
        i = i.replace('\n','')
        #拼接url
        if re.search(r'http',i):
            url=i
        else:
            url='http://' + i+ ':888/pma'
        url_list.append(url)
    main()
    f.close()

