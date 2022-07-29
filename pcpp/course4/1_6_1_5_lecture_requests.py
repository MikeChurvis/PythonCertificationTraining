import requests

reply = requests.get("http://localhost:3000")
print(reply.text)
