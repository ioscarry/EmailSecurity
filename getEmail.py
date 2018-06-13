import requests
import json
import operator
import numpy as np
import re
from bs4 import BeautifulSoup
#抓取 ChinaZ.com 的网站排行：主要是邮件通信的排名
#http://top.chinaz.com/hangye/index_wangluo_youjian.html
def getChinaZ():
    infoDict = {}
    for i in range(1, 5):
        if i == 1:
            url = "http://top.chinaz.com/hangye/index_wangluo_youjian.html"
        else:
            url = "http://top.chinaz.com/hangye/index_wangluo_youjian_" + str(i) + ".html"
        res = requests.get(url)
        print(res)
        soup = BeautifulSoup(res.content, 'html.parser')

        listC = soup.find_all(class_="listCentent")
        for k in BeautifulSoup(str(listC), 'html.parser').find_all("li"):
            print("*********\n")
            print("name:", k.find("a", class_="pr10").text)
            name = k.find("a", class_="pr10").text
            print("link:", k.find("span", class_="col-gray").text)
            link = k.find("span", class_="col-gray").text
            if name not in infoDict.keys():
                infoDict[name] = link

    print(infoDict)
    f = open("email_chinaZ.txt", "w", encoding="UTF-8")
    for key in infoDict:
        f.write(key + " " + infoDict[key] + "\n")
    f.close()

#爬取网易黄页  http://y.mail.163.com/school 中国百强高校邮箱

url="http://y.mail.163.com/school"
res=requests.get(url)
soup=BeautifulSoup(res.content,"html.parser")
info=soup.find_all("li")
f=open("中国百强高校邮箱域名.txt","w",encoding="UTF-8")
nameAll=[]
emailAll=[]
for k in info:
    name=k.find("span",class_="name")
    pattern=re.compile(r'>(.*?)</span')
    nameList=pattern.findall(str(name))
    if(len(nameList)>0):
        print(nameList[0])
        nameAll.append(nameList[0])
    email=k.find("span",class_="mail")

    pattern = re.compile(r'@(.*?)</span')
    emailList=pattern.findall(str(email))
    if(len(emailList)>0):
        print(emailList[0])
        emailAll.append(emailList[0])
for i in range(len(nameAll)):
    f.write(nameAll[i]+" "+emailAll[i]+"\n")
f.close()
