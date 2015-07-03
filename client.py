# Echo client program 
import socket 
 
HOST = ' 10.0.0.1' # According to your server ip address 

PORT = 50007 # The same port as used by the server 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((HOST, PORT)) 
s.sendall('Hello, world') 

data = s.recv(1024) 

s.close() 

print 'Received', repr(data) 



