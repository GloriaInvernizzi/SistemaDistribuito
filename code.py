def is_prime(n):
  n = int(n)
  for i in range(2,n):
    if (n%i) == 0:
      return "False"
  return "True"

import socket
from socket import * 
import sys 

inizio = int(sys.argv[1])
fine = int(sys.argv[2])

HOST = "127.0.0.1"
PORT = 1120

s = socket(AF_INET, SOCK_STREAM)    # create a TCP socket 
s.connect((HOST, PORT))

primi=[]
for i in range (inizio,fine):
  risultato = is_prime(i)
  if risultato == "True":
    primi.append(i) 
print(primi)
request="result"
s.send(request.encode('UTF-8'))
s.send(str(primi).encode('UTF-8'))

request="close"
s.send(request.encode('UTF-8'))
s.close() 