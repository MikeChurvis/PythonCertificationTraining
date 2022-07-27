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

### Connection-oriented vs. Connectionless Communication

**Connection-oriented**: Phonecall model. The caller makes sure the callee is both listening and authorized to receive; only then will data transfer begin. Communication ends when either party hangs up. These are usually done through the TCP/IP.

**Connectionless**: Walkie-talkie model. The broadcaster pushes a 'talk' button and begins speaking. Many others could be listening, but the broadcaster will never know. Communication ends when the broadcaster stops talking. These are usually done through the UDP.

