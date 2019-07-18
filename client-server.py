# Save as client.py
# Message Sender

import json
import socket as newsocket
from socket import *
import getpass
from urllib.request import urlopen
import os


host = "localhost"# set to IP address of target computer
port = 12345
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    #get the username of your machine
    username = getpass.getuser()
    print("\nUSERNAME   :   ", username)

    #get the hostname of your machine
    hostname = newsocket.gethostname()
    print("\nHOSTNAME   :   ", hostname)

    #get the IP address of your machine
    machineIP = newsocket.gethostbyname(hostname)
    print("\nIP ADDRESS :   ", machineIP)

    #get the public IP address and the location
    #open the url and store the response
    url = 'http://ipinfo.io/json'
    response = urlopen(url)

    #convertin JSON encoded response into python objects
    data = json.load(response)

    #fetching and displaying necessary data
    print("\nPUBLIC IP  :   ", data['ip'])
    print("\nCITY       :   ", data['city'])
    print("\nSTATE      :   ", data['region'])
    print("\nCOUNTRY    :   ", data['country'])
    print("\nLOC        :   ", data['loc'])
    print("\nORGANIZATION:  ", data['org'])

    with open("data.txt", "w+") as myfile:
        myfile.write(username+ '\n')
        myfile.write(hostname+ '\n')
        myfile.write(machineIP+ '\n')
        myfile.write(data['ip']+ '\n')

    data = machineIP
    user = username
    host = hostname
    newfile = myfile.encoding
    newuser = user.encode()
    newdata = data.encode()
    newhost = host.encode()
    UDPSock.sendto(newdata, addr)
    UDPSock.sendto(newuser, addr)
    UDPSock.sendto(newhost, addr)
    lanjut = input('Tekan enter atau ketik "exit" untuk keluar : ')
    if lanjut == "exit":
        break
UDPSock.close()
os._exit(0)
