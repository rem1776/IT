import threading
import time
import random
import socket
import sys


    

if __name__ == "__main__":

    try:
        rcs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print(err)

    port = int(sys.argv[2])
    addr = socket.gethostbyname(sys.argv[1])
    server_binding = (addr, port)
    print("Connecting...")
    #rcs.connect(server_binding)
    print("Connected.")

    #read and send hostnames
    nameList = open("PROJI-HNS.txt", "r").readlines()
    for name in nameList:
        rcs.send(name.encode('utf-8'))
        rcs.
    
