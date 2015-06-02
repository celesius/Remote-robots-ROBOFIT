#!/usr/bin/env python

import socket

if __name__ == "__main__":

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 8080))
    s.send('MJPEG:CLIENT\r\n')
    data = s.recv(1024)
    print data

