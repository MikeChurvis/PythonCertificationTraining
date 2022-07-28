# Module 1 - Working with Restful APIs

### Sockets

**Socket**: an endpoint; a point to which data can be sent and from which it is available. Write to a socket to send data through a network. Read from a socket to receive incoming data from the network.
- BSD Socket
- POSIX Socket
- WinSock

A socket is a combination of an IP address and a Port. 

Maximal socket identifier: `255.255.255.255:65535`

##### Socket Domains

**Unix domain (Unix)**: the sockets that communicate between programs working within the same operating system.

**Internet domain (INET)**: the sockets that communicate between programs working between computers connected using a TCP/IP network. It is still possible for two INET sockets on the same OS to communicate.

INET sockets will be the focus of this module.

##### Socket Address

**IP4 address**: 32-bit long value, represented as parts `a.b.c.d` where each part in 0..=255
**IP6 address**: 128-bit long value, successor to IP4, not yet in majority adoption.

**Socket number (service number, port number)**: 16-bit long value ID of a socket in the context of the host machine. Often these are consistent even between different machines; example: `80` for HTTP traffic, `443` for HTTPS traffic. 

### Protocols

**Protocol**: a standardized set of rules by which processes communicate, like a language and customs.

**Protocol Stack**: a set of protocols that cooperate with each other to form a suite of services; said to be "stacked" with the more abstract protocols at higher levels, and the more concrete ones at lower levels.

##### Example: TCP/IP and UDP Protocol Stacks

**Internetwork Protocol (IP)**: 
- Builds a datagram (packet) from a piece of data.
- Throws the datagram at a node.

**Transmission Control Protocol (TCP)**: 
- Shakes hands with the node to make sure it's ready to receive data. 
- Ensures that a two-way stream of data exists for the duration of communication. This is a connection.
- Puts a serial number on each datagram so that the node can reconstruct the original message if packets are received out of order (can also resend lost packets).
- Stops sending data if the connection is lost.

**User Datagram Protocol (UDP)**: 
- Like TCP except it makes no handshake and thus guarantees no connection.
- Does not track packets; cannot resubmit lost packets.
- Less overhead than TCP and thus faster.
- Used for broadcast/multicast models where one node sends data out to any other node that might be listening.

Both the TCP and UDP use the IP to actually send the packets.

##### Connection-oriented vs. Connectionless Communication

**Connection-oriented**: Phonecall model. The caller makes sure the callee is both listening and authorized to receive; only then will data transfer begin. Communication ends when either party hangs up. These are usually done through the TCP/IP.

**Connectionless**: Walkie-talkie model. The broadcaster pushes a 'talk' button and begins speaking. Many others could be listening, but the broadcaster will never know. Communication ends when the broadcaster stops talking. These are usually done through the UDP.

### The `socket` Library

`socket.socket`: socket object, hereforth aliased as `Socket`

`socket.gaierror`: raised if `Socket.connect(...)` cannot marshal a new connection with the server.

`ConnectionRefusedError`: raised if `Socket.connect(...)` was passed a valid server address but an invalid port.

`socket.timeout`: raised if the server does not respond within a certain timeframe (settable with `Socket.settimeout(...)`).

### JSON

- UTF-8 encoded.
- Strings must use doublequote.
- Python's `None` : JSON's `null`.
- Booleans are lowercase.

Encoder function
- `json.dumps(foo, default=fn_foo_encoder)`
- `fn_foo_encoder` must take arg of `type(foo)` and either `return dict` or `raise TypeError`.

Encoder class
- Subclass `json.JSONEncoder` and implement `.default(self, obj) -> dict`. 
- Pass it to `json.dumps(obj, cls=MyJSONEncoder)`.

Decoder function
- `decoder_fn(data: dict) -> type(obj)`.
- Pass it to `json.loads(data: str, object_hook=decoder_fn)`.

Decoder class
```python
class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_who)

    def decode_who(self, d):
        return Who(**d)

some_man = Who('Jane Doe', 23)
json_str = json.dumps(some_man, cls=MyEncoder)
new_man = json.loads(json_str, cls=MyDecoder)
```

### XML

**Document Type Definition (dtd)**: a meta-document whose location is specified in the `<!DOCTYPE document_name (SYSTEM|PUBLIC) "dtd_uri">` tag. Its existence allows the XML parser to check the document's semantic correctness (i.e. the existence and position of certain tags and attributes) against a definition file written in SGML, where otherwise it could only check syntax.

Everything else about DTDs is beyond the scope of this course.

Read:
```python
import xml.etree.ElementTree

cars_for_sale = xml.etree.ElementTree.parse('cars.xml').getroot()
print(cars_for_sale.tag)
for car in cars_for_sale.findall('car'):
    print('\t', car.tag)
    for prop in car:
        print('\t\t', prop.tag, end='')
        if prop.tag == 'price':
            print(prop.attrib, end='')
    print(' =', prop.text)
```

Write/Modify:
```python
import xml.etree.ElementTree

tree = xml.etree.ElementTree.parse('cars.xml')
cars_for_sale = tree.getroot()
for car in cars_for_sale.findall('car'):
    if car.find('brand').text == 'Ford' and car.find('model').text == 'Mustang':
        cars_for_sale.remove(car)
        break
new_car = xml.etree.ElementTree.Element('car')
xml.etree.ElementTree.SubElement(new_car, 'id').text = '4'
xml.etree.ElementTree.SubElement(new_car, 'brand').text = 'Maserati'
xml.etree.ElementTree.SubElement(new_car, 'model').text = 'Mexico'
xml.etree.ElementTree.SubElement(new_car, 'production_year').text = '1970'
xml.etree.ElementTree.SubElement(new_car, 'price', {'currency': 'EUR'}).text = '61800'
cars_for_sale.append(new_car)
tree.write('newcars.xml', method='')
```