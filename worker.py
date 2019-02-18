#!/usr/bin/env python
import subprocess
import sys

try:
    host = sys.argv[1]
    fileName = sys.argv[2]
except:
    exit(1)

fileFullAddress = "/tmp/" + fileName

cmd = 'touch ' + fileFullAddress + "; " + \
 'ping -c 10 ' + host + ' > ' + fileFullAddress + " 2>&1; " + \
 'touch ' + fileFullAddress + ".finished"

proc = subprocess.Popen(cmd,
shell=True, stdin=None ,stdout=None,stderr=None, close_fds=True)
