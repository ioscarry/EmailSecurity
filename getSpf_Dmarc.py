#coding:utf-8
import os
import re
'''
运行系统：linux 环境
'''
def getSPFAndDARC():
    fr=open("alexa排名100邮箱MX_IP.txt","r",encoding="UTF-8")
    lines=fr.readlines()
    for line in lines:
        email=line.strip('\n').split(' ')[1]
        #cmd="dig TXT _dmarc."+email
        cmd = "dig TXT " + email
        os.system(cmd)

def getSPF():
    fr=open("getSPF2.log","r",encoding="UTF-8")
    lines=fr.readlines()
    count=0
    notSupport=[]
    for index in range(len(lines)):
        if lines[index].strip('\n')==";; ANSWER SECTION:":
            index+=1
            print(lines[index])
            if "spf" in lines[index]:
                count+=1
            else:
                notSupport.append(lines[index].strip('\n'))
    print("支持SPF数目",count)
    print("不支持SPF数目:",len(notSupport))
    print(notSupport)


def getDmarc():
    fr=open("getDmarc2.log","r",encoding="UTF-8")
    lines=fr.readlines()
    count=0
    notSupport=[]
    for index in range(len(lines)):
        if lines[index].strip('\n') == ";; ANSWER SECTION:":
            count+=1
            index+=1

            pattern=re.compile("_dmarc\.(.*?)\.edu\.cn")
            str1=lines[index].strip('\n').split(' ')[0]
            emailList = pattern.findall(str(str1))
            if(len(emailList)>0):
                notSupport.append(emailList[0])
            else:
                print(str1)
    print("count:",count)
    print("支持的邮箱:",notSupport)

getDmarc()