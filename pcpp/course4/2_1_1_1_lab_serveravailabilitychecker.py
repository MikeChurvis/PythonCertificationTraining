"""
Requirements:

Write a CLI tool that diagnoses the current state of an HTTP server.

Command signature:
    python <command-name> <ip-address> [<port-number>]

If <port-number> is not given, default is 80.

IP address must match this pattern:
"""

import sys
import socket


def quit_with_error(error_code: int, message: str):
    print(message)
    exit(error_code)


if __name__ == '__main__':
    def main():
        if len(sys.argv) < 2:
            quit_with_error(1, "Invalid Command Syntax: expected 1 or 2 arguments but received zero.")

        address = sys.argv[1]

        if len(sys.argv) >= 3:
            port = sys.argv[2]
            try:
                port = int(port)
            except TypeError:
                quit_with_error(2, f"Invalid Port Number: {port} is not an integer.")

            if port not in range(1, 65536):
                quit_with_error(2, f"Invalid Port Number: {port} is not between 1 and 65535 inclusive.")
        else:
            port = 80

        sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

        try:
            sock.connect((address, port))
            sock.send(bytes(f"HEAD / HTTP/1.1 \r\nHost:{address}\r\n\r\n"))
            response = sock.recv(4096)
            print(response.decode())
        except socket.timeout:
            quit_with_error(3, "Connection Timeout: the server took too long to respond.")
        except (socket.gaierror, ConnectionRefusedError) as other_network_error:
            quit_with_error(4, f"Connection Failed: {type(other_network_error).__name__}")
        finally:
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()


    main()
