import threading
import time
import random
import socket
import sys


def loadTable():
    lines = open("PROJI-DNSTS.txt", "r").readlines()
    table = {}
    for line in lines:
        words = line.split()
        table[words[0]] = (words[1], words[2])
    return table

def recvHostnames(conn):
    msg = ""
    cNames = []
    while "*" not in msg:
        msg = str(conn.recv(100).decode("utf-8"))[:-1]
        cNames.append(msg)
        time.sleep(0.1)
    cNames.pop()
    return cNames

if __name__ == "__main__":

    # load table from file
    table = loadTable()

    # set up socket and listen for connection
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print(err)
    port = int(sys.argv[1])
    sbinding = ('', port)
    cs.bind(sbinding)
    cs.listen(1)
    conn, addr = cs.accept()

    # get hostnames from client
    hnList = recvHostnames(conn)
    print(hnList)
    
    #lookup hostnames and reply, then send end signal
    for name in hnList:
        res = table.get(name)
        time.sleep(0.5)
        if res != None and res[1] == 'A':
            conn.send((name + " " + res[0] + " " + res[1]).encode("utf-8"))
        else:
            conn.send((name + " - Error:HOST NOT FOUND").encode("utf-8"))
    conn.send("***".encode("utf-8"))
