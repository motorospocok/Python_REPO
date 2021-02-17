# MTS matrix contoller
# Can be run from Windows
# Prototype Version 

import socket
import sys
import struct
import time
import binascii

TCP_IP = '192.168.83.50'
TCP_PORT = 4001
BUFFER_SIZE = 1024


val = input("Input e.g A5P13: ")
message1 = val.encode('utf-8')
m1 = message1.hex()
m2 = '02' + m1 + '03'
print(m1)
print(m2)

MESSAGE = binascii.unhexlify(m2)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
s.close()

