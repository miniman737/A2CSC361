#Marcus Ganz V00952336
import sys
import ssl
import socket
import urllib.parse 
import struct

def readFile(filePath):
    with open(filePath, 'rb') as f:
        x = f.readlines()
        # this is just here to test 
#        for y in x:
#            print(y)
        return x


print("the file path that was typed was:", sys.argv[1:])
argument = sys.argv[1:]
tcpFile = argument[0]

print(tcpFile)
capAsList = readFile(tcpFile)




