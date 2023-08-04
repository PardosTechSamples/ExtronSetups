# Tested and confirmed working on Windows 10 / 11.
# 

import sys
import telnetlib
import time



HOST = "192.168.0.1"
SITE1URI = "udp://@238.XXX.XXX.XXX:1234"
SITE1 = "SITE1IP.TXT"
PASSWORD = "ABCDEF\n"


# SMD101Setup will remote into a single device using telnet, adjust the volume level, and load any URI 
Playlist.
def SMD101Setup(HOST, URI, PASSWORD):
    tn = telnetlib.Telnet(HOST)
    time.sleep(1)
    print(tn.read_lazy())
    print(tn.read_until("Password:".encode('utf-8')))
    tn.write(password.encode('utf-8'))

    # Set the volume #
    tn.write("-4V".encode('utf-8'))

    # 1: Load URI Playlist...
    completeString = "\x1bU1*" + URI + "PLYR\x0d"
    tn.write(completeString.encode('utf-8'))

    # 2: Play Playlist...
    tn.write("\x1bS1*1PLYR\x0d".encode('utf-8'))


###########################
##  SMD101 BATCH SETUP   ##
###########################


def runSITE(SITE, URI, PASSWORD): // Static PWD
    f = open(SITE, "r")
    ipList = f.readlines()
    counter = 1

    for i in ipList:
        print("Device # ", counter, i)
        counter += 1
        SMD101Setup(i, URI, PASSWORD)

# RUN SITE 1
# runSITE(SITE1, SITE1URI, PASSWORD)


# Run Single device:
SMD101Setup(HOST, SITE1URI, PASSWORD)
