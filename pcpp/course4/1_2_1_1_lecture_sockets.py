import socket

server_addr = input("What server do you want to connect to? ")
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sock.connect((server_addr, 80))
sock.send(bytes("GET / HTTP/1.1\r\n"
                f"Host: {server_addr}\r\n"
                "Connection: close\r\n\r\n",
                encoding="utf8"))
reply = sock.recv(10000)
sock.shutdown(socket.SHUT_RDWR)
sock.close()
print(repr(reply))