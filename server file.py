from email.header import Header
import socket
import threading 

HEADER = 64
Port = 5060
Server = socket.gethostbyname(socket.gethostname())
addr = (Server, Port)
Format = 'utf-8'
Disconnect_msg = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)

def handle_client(conn, addr):
    print(f"[new connection] {addr} connected.")
    connected = True
    while connected:
        msg_len = conn.recv(HEADER).decode()
        if msg_len:
            msg_LEN = int(msg_len)
            msg = conn.recv(msg_LEN).decode(Format)
            if msg == Disconnect_msg:
                connected = False
            print(f"[{addr}] {msg}")
    conn.close()

def start():
    server.listen()
    print(f"server is listening on {Server}")
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()}")

print("[PROCESSING] SERVER IS STARTING.....")
start()

