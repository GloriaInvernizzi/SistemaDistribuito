from socket import * 
import _thread
#librearia da provare a sostitutire con _thread -> threading

def thread(arg, c):
    print("thread iniziato")
    while True:
        request=c.recv(1024).decode('UTF-8')
        print("request")
        if request== "code":
            send_code(c)
        elif request == "number":
            send_number(c)
        elif request == "result":
            result=c.recv(1024).decode()
            print(f"{result}")
        elif request == "close":
            c.close()
            break
      

def send_code(c):
   c.send(bytes_read.encode('UTF-8'))

def send_number(c):
   intervallo = int(input("Scegli l'intervallo di numeri: "))
   c.send(str(intervallo).encode('UTF-8'))
   
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
while True:
   c, addr = s.accept() 
   _thread.start_new_thread(thread, (i, c))

