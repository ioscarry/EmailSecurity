'''
解析获取的mxtoolbox的网页内容
'''
import re
from bs4 import BeautifulSoup
f=open("slenium网页查询得到的结果2.txt",'r')
res=f.read()
soup=BeautifulSoup(res,"html.parser")

infoList=[]
nameList=[]
responseList=[]
for k in soup.find_all("div",class_="tool-result-body"):
    #print("???????????????????")
    info1=k.find("h3").text
    #print(info1)
    infoList.append(info1)
for k in soup.find_all("tbody"):
    #print("******************")
    listName=[x.text for x in k.find_all("td",class_="table-column-Name")]
    #print(listName)
    listResponse=[x.text for x in k.find_all("td",class_="table-column-Response")]
    #print(listResponse)
    nameList.append(listName)
    responseList.append(listResponse)


# print(infoList)
# print(responseList)
# print(len(infoList))
print(len(nameList))
# print(len(responseList))
count=0
notSupportTls=[]
notSupportIndex=[]
for i in range(len(nameList)):
    name=nameList[i]
    response=responseList[i]
    #获取支持TLS的数目

    if(len(response)>0):
        try:
            index=-1
            index=response.index('OK - Supports TLS.')
            print("index:",index)
            count+=1
        except:
            notSupportTls.append(infoList[i])
            notSupportIndex.append(i)
            print("name:",response)
print("支持数目:",count)
print("不支持:",notSupportTls)
print("不支持数目:",len(notSupportTls))
print("不支持编号:",notSupportIndex)