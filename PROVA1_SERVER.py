from socket import * 
import _thread

def thread(arg, s):
    #print("prova")
    _thread.start_new_thread(thread, (arg, s))
    c, addr = s.accept()                # establish connection with client
    
    #print("thread iniziato")
    while True:
      request=c.recv(1024).decode('UTF-8')
      print(request)
      if request== "code":
         send_code(c)
      elif request == "number":
         print(request)
         send_number(c)
      elif request == "close":
         c.close()
         break
   #c.send(bytes_read.encode('UTF-8'))
   #c.close() 

def send_code(c):
   c.send(bytes_read.encode('UTF-8'))

def send_number(c):
   intervallo = int(input("Scegli l'intervallo di numeri: "))
   for i in range (intervallo):
      c.send(str(i).encode('UTF-8'))
      risultato = c.recv(1024).decode('UTF-8')
      print(str(i) + " è un numero primo? " + risultato)
   
#MAIN-------------------------------

HOST = "127.0.0.1"
PORT  = 1120
#PORT2 = 1140

s = socket(AF_INET, SOCK_STREAM)    # create a TCP socket  
s.bind((HOST, PORT))  
s.listen(5)                         # the number of concurrent connections which have not been accept()    

f = open("code.py", "r")            # reading file 'code.py'
bytes_read = f.read(4096)
f.close()

i=0
thread(i,s)
'''s2 = socket(AF_INET, SOCK_STREAM)   # create a TCP socket  
s2.bind((HOST, PORT2))  
s2.listen(5)                        # the number of concurrent connections which have not been accept()
'''
'''while True:
   _thread.start_new_thread(thread, (i, s))
   ls = input("continuare? y/n ")'''
'''while i<10:
  # Start a new thread and return its identifier
   _thread.start_new_thread(thread, (i, s))
   i=i+1'''


'''primi = []
   # Start a new thread and return its identifier
   _thread.start_new_thread(thread, (arg, s))
   c2, addr = s2.accept()

   intervallo = int(input("Scegli l'intervallo di numeri: "))
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
   c2.close()'''