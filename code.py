def is_prime(n):
  n = int(n)
  for i in range(2,n):
    if (n%i) == 0:
      return "False"
  return "True"
  
  
import socket
import json
from socket import * 

HOST = "192.168.198.236"
PORT = 1140

s = socket(AF_INET, SOCK_STREAM)    # create a TCP socket 
s.connect((HOST, PORT))

print("code partito!")

while True:
	numero = s.recv(1024)
	numero = numero.decode('UTF-8')

	print("numero ", numero)
	risultato = is_prime(numero)    

	#s.send(bytes(risultato, 'UTF-8'))
	s.send(risultato.encode('UTF-8'))

s.close()
    

    
