from select import select
from socket import * 
from _thread import *
import threading

# Define a function for the thread
def threaded( c ):
   while True:
      # data received from client
      data = c.recv(1024)
      if not data:
         print('Bye')   
         # lock released on exit
         print_lock.release()
         break
      # send back string to client
      c.sendall(bytes_read.encode('UTF-8'))
   # connection closed
   c.close()
   
def manda_numero(c, num):
   c.send(num.encode('UTF-8'))
   
#MAIN-------------------------------
print_lock = threading.Lock()
host = "192.168.198.236"
port = 1126
s = socket(AF_INET, SOCK_STREAM)    # create a TCP socket  
s.bind((host, port))  
s.listen(5)                         #the number of concurrent connections which have not been accept()    

f = open("code.py", "r")
bytes_read = f.read(4096)

while True:
   # establish connection with client
   c, addr = s.accept()
   # lock acquired by client
   print_lock.acquire()
   print('Connected to :', addr[0], ':', addr[1])
 
   # Start a new thread and return its identifier
   start_new_thread(threaded, (c,))
   
   port = 1134
   s2 = socket(AF_INET, SOCK_STREAM)    # create a TCP socket  
   s2.bind((host, port))  
   s2.listen(5)                         #the number of concurrent connections which have not been accept()
   while True:
      c2, addr = s2.accept()
      manda_numero(c2, "15")
      print("15 mandato")
      risultato = c2.recv(1024)
      print(risultato.decode('UTF-8'))
      c2.close()