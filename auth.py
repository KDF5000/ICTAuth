#!/usr/bin/env python
# encoding=utf8 

"""
目的：使用urllib2封装一个网络请求库，提供get和post方法
"""
import hashlib
import sys,os
import urllib
import urllib2

reload(sys)
sys.setdefaultencoding('utf8')

class Net(object):

    @staticmethod
    def get(url,params=dict(), header=dict()):
        newUrl = url + "?" + urllib.urlencode(params)
        req = urllib2.Request(newUrl, headers=header)
        r = urllib2.urlopen(req)
        return r.read()

    @staticmethod
    def post(url, params=dict(), header=dict()):
        data = urllib.urlencode(params)
        req = urllib2.Request(url, data=data, headers=header)
        r = urllib2.urlopen(req)
        return r.read()

def do_login(username, password):
    #pass_str = hashlib.md5("*****").hexdigest()
    #password = pass_str[8:24]
    data = {"action":"login",
            "username":username, 
            "password":password,
            "ac_id":1,
            #"user_ip": "10.30.5.132",
            #"ip": "10.30.5.132",
            "drop":0,
            "type": 1,
            "n": 100,
            "ajax": 1
            }

    headers = {"Content-Type":"application/x-www-form-urlencoded"}
    res = Net.post("https://gw.ict.ac.cn/srun_portal_pc.php?ac_id=1&",params=data,header=headers)
    print res

def do_logout(username, password):
    data = {
            "action":"logout",
            "username":username,
            "password":password,
            "drop":0,
            "type":1,
            "n":1,
            "ajax":1,
    }

    headers = {"Content-Type":"application/x-www-form-urlencoded"}
    msg = Net.post("https://gw.ict.ac.cn/srun_portal_pc.php?ac_id=1&",params=data, header=headers)
    print msg

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print "Usage: python auth.py [login|logout] username password"
        sys.exit()
    cmd = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    if cmd == 'login':
        # print "Login..."
        do_login(username,password)
    else:
        # print "Logout..."
        do_logout(username, password)
