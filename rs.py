import threading
import time
import random
import socket
import sys


def loadTable():
    lines = open("PROJI-DNSRS.txt", "r").readlines()
    TShostname = lines.pop()
    table = {}
    for line in lines:
        words = line.split()
        table[words[0]] = (words[1], words[2])
    return (table, TShostname)

def recvHostnames(conn):
    msg = ""
    cNames = []
    while "***" not in msg:
        msg = str(conn.recv(100).decode("utf-8"))
        cNames.append(msg)
    cNames.pop()
    return cNames

if __name__ == "__main__":

    # load table from file
    tableData = loadTable()
    table = tableData[0]
    TShostname = tableData[1]

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

    #lookup hostnames
    for name in hnList:
        res = table.get(name)
        time.sleep(0.1)
        if res != None and res[1] == 'A':
            conn.send((name + " " + res[0] + " " + res[1]).encode("utf-8"))
        else:
            conn.send((TShostname + " NS").encode("utf-8"))
