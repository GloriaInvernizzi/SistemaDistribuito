from socket import * 
import subprocess

HOST = "127.0.0.1"
PORT = 1120

s = socket(AF_INET, SOCK_STREAM)    # create a TCP socket 
s.connect((HOST, PORT))
request="code"
s.send(request.encode('UTF-8'))
# message received from server
data = s.recv(1024)
f = open("code.py", "w")
f.write(str(data.decode('UTF-8')))
f.close()

while True:
    subprocess.run(['python', 'code.py'])

    # ask the client whether he wants to continue
    ans = input('\nDo you want to continue(y/n) :')
    if ans == 'y':
        continue
    else:
        request="close"
        s.send(request.encode('UTF-8'))
        break

# close the connection
s.close()