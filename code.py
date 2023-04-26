def is_prime(n):
  n = int(n)
  for i in range(2,n):
    if (n%i) == 0:
      return "False"
  return "True"
  
  
import socket
import json
from socket import * 
import sys

#nome_script, primo = sys.argv

HOST = "127.0.0.1"
PORT = 1140

s = socket(AF_INET, SOCK_STREAM)    # create a TCP socket 
s.connect((HOST, PORT))

print("code partito!")


while True:
	numero = s.recv(1024)
	if not numero:
		print('comunicazione conclusa')   
		break
	numero = numero.decode('UTF-8')
	print("numero ", numero)
	risultato = is_prime(numero)    

	#s.send(bytes(risultato, 'UTF-8'))
	s.send(risultato.encode('UTF-8'))

s.close()
