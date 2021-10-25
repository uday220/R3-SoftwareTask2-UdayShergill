import socket
TCP_IP = '127.0.0.1'
TCP_PORT = 2003
BUFFER_SIZE = 2048  
closer = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(2)
conn, addr = s.accept()
while closer <= 0:
    data = conn.recv(BUFFER_SIZE)
    data = data.decode("ascii")
    print(data)
    closer += 1