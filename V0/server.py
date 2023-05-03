from socket import * 
import _thread
import logging

def thread(arg, s):
   c, addr = s.accept()                # establish connection with client
   print("thread iniziato")
   c.send(bytes_read.encode('UTF-8'))
   #c.close() 
    
def manda_numero(c, num):
   num = str(num)
   c.send(num.encode('UTF-8'))
   
#MAIN-------------------------------

HOST = "127.0.0.1"
PORT  = 1120
PORT2 = 1140

s = socket(AF_INET, SOCK_STREAM)    # create a TCP socket  
s.bind((HOST, PORT))  
s.listen(5)                         # the number of concurrent connections which have not been accept()    

s2 = socket(AF_INET, SOCK_STREAM)   # create a TCP socket  
s2.bind((HOST, PORT2))  
s2.listen(5)                        # the number of concurrent connections which have not been accept()

f = open("code.py", "r")
bytes_read = f.read(4096)
f.close()

arg = ""

while True:
   primi = []
   # Start a new thread and return its identifier
   _thread.start_new_thread(thread, (arg, s))
   c2, addr = s2.accept()

   #intervallo = int(input("Scegli l'intervallo di numeri: "))
   intervallo = 6
   for i in range (intervallo):
      manda_numero(c2, i)
      risultato = c2.recv(1024).decode('UTF-8')
      if (risultato=="True" and i>1):
         primi.append(i) 
         #print(str(i) + " è primo")
   print(primi)
   primi_s = ' '.join(str(x) for x in primi)

   f = open("primi.json", "w")
   f.write("Primi fino a " + str(intervallo) + ":\n")
   f.close()
   f = open("primi.json", "a")
   f.write(primi_s)
   f.close()    
   c2.close()