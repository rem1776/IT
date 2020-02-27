import threading
import time
import random
import socket
import sys


if __name__ == "__main__":

    # set up socket and listen for connection
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print(err)
    port = int(sys.argv[1])
    sbinding = ('', port)
    cs.bind(sbinding)
    cs.listen(1)

    # accept connection and recieve hostnames from client
    conn, addr = cs.accept()
    msg = ""
    cNames = []
    while "***" not in msg:
        msg = str(conn.recv(100).decode("utf-8")))
        cNames.append(msg)

    #cNames.pop()
    print(cNames)

