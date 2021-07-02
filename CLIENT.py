#client
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#server ip
sip="111.11.11.1"
#server port
sport=5656
s.sendto(b"hello",(sip,sport))
