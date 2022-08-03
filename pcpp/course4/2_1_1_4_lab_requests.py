import sys
import requests

address = None
port = None

args = sys.argv[1:3]

if len(args) == 0:
    print("[ERROR] Bad command syntax: no web address specified.")
    exit(1)

address = args[0]

if len(args) == 2:
    try:
        port = int(args[1])
    except TypeError:
        print("[ERROR] Bad command syntax: port (the optional second argument) must be an integer.")
        exit(1)

    if port not in range(1, 65536):
        print("[ERROR] Bad port number: port must be between 1 and 65535 inclusive.")
        exit(2)
else:
    port = 80

response = None
an_error_occurred = True

try:
    response = requests.head(f"http://{address}:{port}")
except requests.exceptions.InvalidURL:
    print(f"[ERROR] The url given is invalid.")
except requests.exceptions.ConnectTimeout:
    print(f"[ERROR] The request timed out while trying to connect to the server.")
except requests.exceptions.ReadTimeout:
    print(f"[ERROR] The server did not respond in the allotted amount of time.")
except requests.exceptions.ConnectionError:
    print(f"[ERROR] Could not establish a connection to the server. Check the given URL and port number.")
except requests.exceptions.HTTPError as error:
    print(f"[ERROR] The target server responded with an error: {error.errno}")
except requests.exceptions.RequestException as error:
    print(f"[ERROR] An ambiguous exception occurred within the `requests` library. Details:\n\n{error}")
else:
    an_error_occurred = False

if an_error_occurred or response is None:
    exit(3)

if response.ok:
    print(f"[SUCCESS] The server at {address} is available.")
