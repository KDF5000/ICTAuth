#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
目的：使用urllib2封装一个网络请求库，提供get和post方法
"""
import requests as req
import hashlib
import sys,os
class Net(object):

    @staticmethod
    def get(url,params=dict(), header=dict()):
        r = req.get(url,params=params)
        return r.text

    @staticmethod
    def post(url, params=dict(), header=dict()):
        r = req.post(url, data=params)
        return r.text

def do_login():
    pass_str = hashlib.md5("*****").hexdigest()
    password = pass_str[8:24]
    data = {"username":"kongdefei", "password":password,"drop":0, "type":1, "n":100}
    headers = {"Content-Type":"application/x-www-form-urlencoded"}
    uid = Net.post("http://159.226.39.22/cgi-bin/do_login",params=data,header=headers)
    print uid
    with open("uid", 'w') as fw:
        fw.write(uid)

def do_logout():
    if not os.path.isfile("uid"):
        print "Please confirm that your account are on line"
        sys.exit()
    fp = open('uid')
    uid = fp.readline().strip()
    
    if uid == "":
        print "Please confirm that your account are on line"
        sys.exit()

    data = {"uid":uid}
    headers = {"Content-Type":"application/x-www-form-urlencoded"}
    msg = Net.post("http://159.226.39.22/cgi-bin/do_logout",params=data, header=headers)
    print msg

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print "Usage: python auth.py [login|logout]"
        sys.exit()
    cmd = sys.argv[1]
    if cmd == 'login':
        # print "Login..."
        do_login()
    else:
        # print "Logout..."
        do_logout()
