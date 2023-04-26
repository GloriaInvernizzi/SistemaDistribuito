from socket import * 
import subprocess
#HOST = "192.168.198.236"
HOST= "127.0.0.1"
PORT = 1132

s = socket(AF_INET, SOCK_STREAM)    # create a TCP socket 
s.connect((HOST, PORT))

#numero = s.recv(1024).decode('UTF-8')
message="INIZIO COMUNICAZIONE CLIENT-SERVER"
while True:
 
    # message sent to server
    s.send(message.encode('UTF-8'))

    # message received from server
    data = s.recv(1024)

    # print the received message
    # here it would be a reverse of sent message
    print('Received from the server :', str(data.decode('UTF-8')))
    f= open("code.py","w")
    f.write(str(data.decode('UTF-8')))
    f.close()
    subprocess.run(["python","code.py"])
    # ask the client whether he wants to continue
    ans = input('\nDo you want to continue(y/n) :')
    if ans == 'y':
        continue
    else:
        break
    # close the connection
s.close() 