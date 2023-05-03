def is_prime(n):
  n = int(n)
  for i in range(2,n):
    if (n%i) == 0:
      return "False"
  return "True"

import socket
from socket import * 

HOST = "127.0.0.1"
PORT = 1120

s = socket(AF_INET, SOCK_STREAM)    # create a TCP socket 
s.connect((HOST, PORT))
request="number"
s.send(request.encode('UTF-8'))
print("code partito!")

numero = s.recv(1024).decode()
print("Numero ricevuto "+ numero)
primi=[]
for i in range (int(numero)):
  risultato = is_prime(i)
  if risultato == "True":
    primi.append(i) 

request="result"
s.send(request.encode('UTF-8'))
s.send(str(primi).encode('UTF-8'))
request="close"
s.send(request.encode('UTF-8'))
s.close() 