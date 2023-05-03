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
    request= "number"
    s.send(request.encode('UTF-8'))
    numero = int(s.recv(1024).decode())
    print(f"Numero ricevuto {numero}")

    Range=int(numero/4)
    for i in range (4):
        if i == 3:
            fine= numero
            inizio = 0
        else:
            fine= numero
            inizio = numero - Range
        numero= numero - Range
        subprocess.run(['python', 'code.py',str(inizio),str(fine)])

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