# -*- coding: utf-8 -*-
'''
通过网页的mxtoolbox获取邮箱的信息
'''
import time
import requests
from pandas import Series, DataFrame

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
fr=open("中国百强高校邮箱MX_IP.txt","r",encoding="UTF-8")
driver=webdriver.Firefox()
driver.get("https://mxtoolbox.com/SuperTool.aspx#")
print("等待手动选择框。。。")
time.sleep(8)
lines=fr.readlines()

for k in lines[0:]:
    line=k.strip('\n').split(' ')[3]
    print("查询IP:",line)
    try:
        driver.find_element_by_id("txtInput2").clear()
        driver.find_element_by_id("txtInput2").send_keys(line)
        driver.find_element_by_id("btnAction3").click()
        print("开始休息15s...")
        time.sleep(30)
    except:
        print("还没加载完全!",line)
        break



time.sleep(15)
fw=open("slenium网页查询得到的结果.txt","w",encoding="UTF-8")
fw.write(driver.find_element_by_id("lblResult").get_attribute('innerHTML'))
fw.close()
#print(driver.find_element_by_id("lblResult").get_attribute('innerHTML'))
