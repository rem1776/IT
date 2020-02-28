import threading
import time
import random
import socket
import sys

def createTSSocket(hostname):
    # set up socket and connect
    try:
        rcs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print(err)
    port = int(sys.argv[3])
    addr = socket.gethostbyname(hostname)
    server_binding = (addr, port)
    rcs.connect(server_binding)
    return rcs

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

    #read and send hostnames
    nameList = open("PROJI-HNS.txt", "r").readlines()
    for name in nameList:
        name = name.lower()
        rcs.send(name[:-1].encode('utf-8'))
        time.sleep(0.05)
    rcs.send("***".encode('utf-8'))
    
    #print(nameList)


    #get replies, write if resolved, send to TS if not
    resFile = open("RESOLVED.txt", "w")
    tsConn = None
    tsQueries = []
    tsHostname = "localhost" 

    for name in nameList:
        name = name.lower()
        time.sleep(0.1)
        reply = str(rcs.recv(100).decode('utf-8'))
        if(reply[-2:] == 'NS'):
            tsQueries.append(name)   
            tsHostname = reply.split()[0]
        else:
            resFile.write(reply + "\n")
    
    time.sleep(1)
    # send to TS
    if(tsQueries != None):
        tsConn = createTSSocket(tsHostname)
    for q in tsQueries:
        tsConn.send(q.encode("utf-8"))
        time.sleep(0.1)
    tsConn.send("***".encode("utf-8"))
    # send end signal to ts server if connected and receive replies 
    if tsConn != None:
        msg = tsConn.recv(100).decode("utf-8")
        while "***" not in msg:
            time.sleep(0.5)
            resFile.write(msg + "\n")
            msg = tsConn.recv(100).decode("utf-8")


    # close connections
    rcs.close()
    tsConn.close()
