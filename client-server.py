# Save as client-server.py
# Message Sender
# PUT THIS FILE IN YOUR RASPBERRY PI

import socket as newsocket
from socket import *
import os


host = "localhost" # set to IP address of target computer (you can use localhost as well) 
port = 12345
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)

while True:
    
    # yourdata is actually your data that you want to send to server.py
    data = yourdata
    
    # optional code to encode your data into a string CMIIW
    newdata = data.encode()
    
    # use this function to send your data to server.py
    UDPSock.sendto(newdata, addr)
    
UDPSock.close() # ignore this code
os._exit(0) # ignore this code
