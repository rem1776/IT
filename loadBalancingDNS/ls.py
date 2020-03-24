import threading
import time
import random
import socket
import sys


def setUpSock(port):
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print(err)
    sbinding = ('', port)
    cs.bind(sbinding)
    cs.listen(1)
    conn, addr = cs.accept()
    return conn

def recvClientQuery(sock):
    query = None
    query = sock.recv(50).decode("utf-8")
    time.sleep(0.01)
    return query

def queryTS(query):
    #TODO
    return None

if __name__ == "__main__":

    # set up socket and listen for connection
    clientConn = setUpSock(int(sys.argv[1]))
    # get hostnames from client
    query = None
    while query != "END":
        query = recvClientQuery(clientConn)
        queryTS(query)
        print(query)

    # close connection
    clientConn.close()
