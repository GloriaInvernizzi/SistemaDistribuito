import socket
from socket import * 
import _thread
def is_prime(n):
  n = int(n)
  for i in range(2,n):
    if (n%i) == 0:
      return "False"
  return "True"

def thread(arg, socket, inizio,fine):
  print("inizio il thread" + str(inizio) + str(fine))
  primi=[]
  for i in range(inizio,fine):
    risultato = is_prime(i)
    if risultato == "True":
      primi.append(i) 
  request="result"
  socket.send(request.encode('UTF-8'))
  socket.send(str(primi).encode('UTF-8'))
  print(primi)

#----MAIN
HOST = "127.0.0.1"
PORT = 1120
s = socket(AF_INET, SOCK_STREAM)    # create a TCP socket 
s.connect((HOST, PORT))
request="number"
s.send(request.encode('UTF-8'))
print("code partito!")
numero = int(s.recv(1024).decode())
print("Numero ricevuto "+ str(numero))
arg=""

while True:
  if numero <= 1000:
    _thread.start_new_thread(thread, (arg, s, 0, numero))    
    break
  else:
    _thread.start_new_thread(thread, (arg, s, numero-1000, numero))  
    numero = numero - 1000
request="close"
s.send(request.encode('UTF-8'))
s.close() 