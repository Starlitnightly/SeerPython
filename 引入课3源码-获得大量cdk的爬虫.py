# -*- coding: utf-8 -*-
"""
Created on Sat May  2 17:57:43 2020

@author: FernandoZeng
"""

import requests
import time
 
header={
        'Host': 'huodong2.4399.com',\
        'Connection': 'keep-alive',\
        'Content-Length': '38',\
        'Accept': 'application/json, text/javascript, */*; q=0.01',\
        'Origin': 'http://huodong2.4399.com',\
        'X-Requested-With': 'XMLHttpRequest',\
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',\
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',\
        'Referer': 'http://huodong2.4399.com/gifts/2019znq_17.html',\
        'Accept-Encoding': 'gzip, deflate',\
        'Accept-Language': 'zh-CN,zh;q=0.9',\
        }
 
loginurl='http://ptlogin.4399.com/ptlogin/login.do?v=1'
logindata={'loginFrom':'uframe',\
    'postLoginHandler':'refreshParent',\
    'layoutSelfAdapting':'true',\
    'externalLogin':'qq',\
    'displayMode':'popup',\
    'layout':'vertical',\
    'appId':'huodong',\
    'gameId':'',\
    'css':'',\
    'redirectUrl':'',\
    'sessionId':'',\
    'mainDivId':'popup_login_div',\
    'includeFcmInfo':'false',\
    'userNameLabel':'4399%E7%94%A8%E6%88%B7%E5%90%8D',\
    'userNameTip':'%E8%AF%B7%E8%BE%93%E5%85%A54399%E7%94%A8%E6%88%B7%E5%90%8D',\
    'welcomeTip':'%E6%AC%A2%E8%BF%8E%E5%9B%9E%E5%88%B04399',\
    'username':'账号',\
    #此处修改为4399用户名
    'password':'密码',\
    #此处修改为4399账户密码
    'autoLogin':'on'}
page=requests.Session()
page.headers=header
page.post(loginurl,data=logindata)
 
url="http://huodong2.4399.com/gifts/ajax.php"
d={'op':'taoma','hd_id':'26','t':'0.2566171214281707'}
while(True):
     
    text = page.post(url,data=d).text 
     
    if(text.find("taoma_out_limit")!=-1):
        time.sleep(30)
    else:
        f=open('list.txt','a')
        malist=[text[29:45]+'\n',text[48:64]+'\n',text[67:83]+'\n']
        print(malist)
        f.writelines(malist)
        f.close()