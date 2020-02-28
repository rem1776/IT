import threading
import time
import random
import socket
import sys


if __name__ == "__main__":

    # set up socket and connect
    try:
        rcs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print(err)
    port = int(sys.argv[2])
    addr = socket.gethostbyname(sys.argv[1])
    server_binding = (addr, port)
    rcs.connect(server_binding)
    print("Client Connected.")

    #read and send hostnames
    nameList = open("PROJI-HNS.txt", "r").readlines()
    for name in nameList:
        rcs.send(name[:-1].encode('utf-8'))
        time.sleep(0.1)
    rcs.send("***".encode('utf-8'))
    
    #get replies
    for name in nameList:
        time.sleep(0.1)
        reply = str(rcs.recv(100).decode('utf-8'))
        print(reply)
