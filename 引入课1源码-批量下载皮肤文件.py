# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 00:31:17 2020

@author: 星夜
"""
#库，相当于一个文具盒
import os
import requests


#头文件
head={
       'Accept-Language':'zh-CN',
       'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
       'Accept-Encoding':'gzip, deflate',
       'Connection':'Keep-Alive',
       }

#一个循环
for i in range(1,100):
    
    #打开官网下载swf
    swf=requests.get('http://seer.61.com/resource/fightResource/pet/swf/'+str(i)+'.swf',verify=False,headers=head)
   
    #保存swf
    with open(os.getcwd()+'\\seer\\'+str(i)+'.swf','wb') as f:
        f.write(swf.content)
