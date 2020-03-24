import threading
import time
import random
import socket
import sys

def createSocket(hostname, port):
    # set up socket and connect
    try:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print(err)
    addr = socket.gethostbyname(hostname)
    server_binding = (addr, port)
    conn.connect(server_binding)
    return conn

def queryLS(name, sock):
    sock.send(name[:-1].encode('utf-8'))
    #reply = None
    #while reply is None:
    time.sleep(0.01)
    #    reply = str(sock.recv(50).decode('utf-8'))
    #return reply

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Wrong number of arguments.")
        sys.exit(-1)
    # set up socket and connect
    lsSock = createSocket(sys.argv[1] , int(sys.argv[2]))

    #read files
    nameList = open("PROJ2-HNS.txt", "r").readlines()
    resFile = open("RESOLVED.txt", "w")

    for name in nameList:
        name = name.lower()
        reply = queryLS(name, lsSock)
        #resFile.write(reply + "\n")
    
    lsSock.close()
