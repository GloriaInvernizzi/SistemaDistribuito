import socket

HOST = "127.0.0.1"
PORT = 1120

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

numero = s.recv(1024).decode('UTF-8')
    
print(numero)
'''print(type(numero))

converted_num = int(float(numero))
print(type(converted_num))

'''

s.close()
