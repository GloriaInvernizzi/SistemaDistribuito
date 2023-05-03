from socket import * 
import subprocess

HOST = "127.0.0.1"
PORT = 1121

s = socket(AF_INET, SOCK_STREAM)    # create a TCP socket 
s.connect((HOST, PORT))
#message="ciao bellooo"

while True:
    # message sent to server
    #s.send(message.encode('UTF-8'))
    # message received from server
    data = s.recv(1024)

    f = open("code.py", "w")
    f.write(str(data.decode('UTF-8')))
    f.close()
    
    subprocess.run(['python3', 'code.py'])

    # ask the client whether he wants to continue
    ans = input('\nDo you want to continue(y/n) :')
    if ans == 'y':
        continue
    else:
        break

# close the connection
s.close()