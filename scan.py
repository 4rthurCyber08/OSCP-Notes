#!/bin/python3

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
  target = socket.gethostbyname(sys.argv[1])
else:
   print('Invalid amount of arguments')

print('-' * 50)
print('Scanning target '+ target)
print('Time started '+ str(datetime.now()))

try:
  for port in range(50,85):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target.port))
    if result == 0
      print(f'Port {port} is open')
    s.close()
except KeyboardInterrupt:
  print('Exit Program')
  sys.exit()
except socket.gaierror:
  sys.exit()
except socket.error:
  sys.exxit()


