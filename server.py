# Save as server.py
# Message Receiver
from socket import *
import sys
import json

# creates file when the file is doesn't exists
try:
    open("json_file.json")
except FileNotFoundError:
    open("json_file.json", 'w')

#Host a server
host = "192.168.1.10" # use your host setting 
port = 12345 
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print("Waiting to receive messages...")

# creates a dict to keep your data from raspi
newdata = {}
newdata['sensor'] = []

while True:
    (data, addr) = UDPSock.recvfrom(buf) # this is a function to retrieve your data from your client
    
    # optional codes
    print("Received message 1 : Jarak air : " + str(data.split()[-9]))
    print("Received message 2 : Tinggi air : " + str(data.split()[-5]))
    print("Received message 3 : Status gerbang : " + str(data.split()[-1]))
    data = data.decode()

    # appends your recieved data to sensor dict
    newdata['sensor'].append\
        (
            {
             'jarak' : data.split()[-9],
             'tinggi' : data.split()[-5],
             'status' : data.split()[-1],
             }
        )
    
    # this is the function to write your data from your client as JSON file and save it to specific dir
    for data in newdata:
        with open(r"..\yourpathproject\raspi\raspiapp\static\json_file.json", "w") as file_write:
            json.dump(newdata, file_write, indent=4)

UDPSock.close() # ignore this code
os._exit(0) # ignore this code
