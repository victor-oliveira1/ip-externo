#!/bin/python3
from urllib.request import urlopen

req = urlopen('http://myexternalip.com/raw')
ip = req.read().decode().split()[0]

print(ip)
