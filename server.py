from base64 import encode
from select import select
import socket
import getpass
import _thread
import time
import json

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 1120

print ('In attesa di clienti...')
print ('Per chiudere il server premere Ctrl+C')

try:
   while True: 
      f = open("code.py")
      code = f.read()

      s.listen(2)
      ready, _, _=select([s],[],[], 1)
      if ready:
         s.accept()
         s.send(bytes(code, 'UTF-8'))

   # Create two threads as follows
   '''try:
      _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
      _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
      
   except:
      print ("Error: unable to start thread")'''

except KeyboardInterrupt:
    print("\nChiusura server")
    s.close()

