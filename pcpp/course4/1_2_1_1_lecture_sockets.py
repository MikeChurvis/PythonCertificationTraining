import socket as socketlib
from socket import socket as Socket

server_addr = input("What server do you want to connect to? ")
sock = Socket(family=socketlib.AF_INET, type=socketlib.SOCK_STREAM)

sock.connect((server_addr, 80))
sock.send(bytes("GET / HTTP/1.1\r\n"
                f"Host: {server_addr}\r\n"
                "Connection: close\r\n\r\n",
                encoding="utf8"))
reply = sock.recv(10000)

print(repr(reply))

sock.shutdown(socketlib.SHUT_RDWR)
sock.close()

