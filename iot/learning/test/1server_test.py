#!/usr/bin/python
# -*- coding:UTF-8 -*-
import socket

s=socket.socket()
host = socket.gethostname() # get the host name
port = 12345 # set the port
s.bind((host,port)) # attach the port to the host
s.listen(5) # waiting for the connection

while True:
    c,addr = s.accept() # setup the connection
    print("connection location:", addr)
    c.send("test success!")
    c.close() # shutdown the connection
