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

numero = s.recv(1024)
print("Numero ricevuto")

while numero!="":
	risultato = is_prime(numero)    
	s.send(risultato.encode('UTF-8'))
	numero = s.recv(1024)
	numero = numero.decode('UTF-8')

s.close()    