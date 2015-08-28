__author__ = 'Daeho'
# -*- coding: utf-8 -*-
from socket import *
svrSock = socket(AF_INET, SOCK_STREAM)
svrSock.connect(('127.0.0.1',2000))
svrSock.send(b'20133269')