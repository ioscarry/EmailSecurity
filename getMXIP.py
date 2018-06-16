#coding:utf-8
#build by  wuyy
#2018-06-13

import socket
import dns.resolver

#根据邮件 MX记录解析域名
def getIp(url):
    try:
        ip=socket.gethostbyname(url)
        return ip
    except:
        print("this URL 2 IP ERROR ")
        return ""

#获取域名的  MX记录
def getMX(domain="tsinghua.edu.cn"):
    MX = dns.resolver.query(domain, 'MX')
    exchangeList=[]
    for i in MX:
        #print('MX preference =', i.preference, 'mail exchanger =', i.exchange)
        exchangeList.append(i.exchange)
    return exchangeList


if __name__=="__main__":
    fr=open("alexa排名100邮箱.txt",encoding="UTF-8")
    fw=open("alexa排名100邮箱MX_IP.txt","w",encoding="UTF-8")

    lines=fr.readlines()
    for line in lines:
        info=line.strip('\n').split(' ')
        #print(x)
        try:
            print("域名：",info[-1])
            exchangeList=getMX(info[-1])
            #获取第一个 MX记录
            l1=exchangeList[0]
            mx=str(l1)[:-1]
            print("mx:",mx)
            ip1=getIp(mx)
            print(ip1)
            fw.write(info[0]+" "+info[1]+" "+mx+" "+ip1+"\n")
        except:
            print("出现问题")

    fr.close()
    fw.close()