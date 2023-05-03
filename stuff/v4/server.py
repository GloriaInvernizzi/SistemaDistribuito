from socket import * 
import _thread

#https://docs.pycom.io/firmwareapi/micropython/_thread/

def thread(arg, s):
   c, addr = s.accept()		            # establish connection with client

   print("thread iniziato")
   c.send(bytes_read.encode('UTF-8'))
   # connection closed per poter permettere a un altro client di accedere alla stessa porta??
   #c.close() 
    
def manda_numero(c, num):
   num = str(num)
   c.send(num.encode('UTF-8'))
   
#MAIN-------------------------------

HOST = "127.0.0.1"
PORT  = 1121
PORT2 = 1141

s = socket(AF_INET, SOCK_STREAM)    # create a TCP socket  
s.bind((HOST, PORT))  
s.listen(5)                         # the number of concurrent connections which have not been accept()    

s2 = socket(AF_INET, SOCK_STREAM)    # create a TCP socket  
s2.bind((HOST, PORT2))  
s2.listen(5)                         #the number of concurrent connections which have not been accept()

f = open("code.py", "r")
bytes_read = f.read(4096)
f.close()

arg = ""

while True:
   # Start a new thread and return its identifier
   _thread.start_new_thread(thread, (arg, s))
   c2, addr = s2.accept()

   intervallo = int(input("Scegli l'intervallo di numeri: "))
   for i in range (intervallo):
      manda_numero(c2, i)
      risultato = c2.recv(1024).decode('UTF-8')
      if risultato=="True":
         print(str(i) + " è primo")
   c2.close()