# Save as server.py
# Message Receiver
from socket import *
import sys
import json
import re

try:
    open("json_file.json")
except FileNotFoundError:
    open("json_file.json", 'w')

#Host a server
host = "192.168.1.10"
port = 12345
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print("Waiting to receive messages...")
newdata = {}
newdata['sensor'] = []

while True:
    (data, addr) = UDPSock.recvfrom(buf)
    print("Received message 1 : Jarak air : " + str(data.split()[-9]))
    print("Received message 2 : Tinggi air : " + str(data.split()[-5]))
    print("Received message 3 : Status gerbang : " + str(data.split()[-1]))
    data = data.decode()
    data.split()


    newdata['sensor'].append\
        (
            {
             'jarak' : data.split()[-9],
             'tinggi' : data.split()[-5],
             'status' : data.split()[-1],
             }
        )
    for data in newdata:
        with open(r"C:\Users\ASUS ROG\PycharmProjects\little\Django\django_project\first_project\static\json_file.json", "w") as file_write:
            json.dump(newdata, file_write, indent=4)
        if data == "exit":
            sys.exit()

UDPSock.close()
os._exit(0)
