import socket

#for udp protocol
protocol = socket.SOCK_DGRAM
#ipv4 add
address = socket.AF_INET

s = socket.socket(add,protocol)

sip="111.11.11.1"
sport=5656
s.bind((sip,sport))

while True:
   x =s.recvfrom(1024)
   print(x)
