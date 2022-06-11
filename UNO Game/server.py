import socket
from threading import Thread

host = "0.0.0.0"
port = 5002 
separate  = "<SEP>" 

c_sockets = set()
s_data = socket.socket()
s_data.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s_data.bind((host, port))

s_data.listen()
print(f"[*] Listening as {host}:{port}")
def listen_for_client(cs):
    while True:
        try:
            msg = cs.recv(1024).decode()
        except Exception as e:
            print(f"[!] Error: {e}")
            c_sockets.remove(cs)
        else:
            msg = msg.replace(separate, ": ")
        for c_socket in c_sockets:
            c_socket.send(msg.encode())

while True:
    c_socket, c_address = s_data.accept()
    print(f"[+] {c_address} connected.")
    c_sockets.add(c_socket)
    t = Thread(target=listen_for_client, args=(c_socket,))
    t.daemon = True
    t.start()
