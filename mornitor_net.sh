#!/bin/bash

ping -c 3 -t 5 www.baidu.com > /dev/null
if [ $? != 0 ];then
   ret=$(/usr/bin/env python /home/pi/Documents/Coding/ICTAuth/auth.py login kongdefei devin123)
   echo "[`date`]: Reconnect to ICT, uid: $ret"
else
   echo "[`date`]: Connected to the internet"
fi
