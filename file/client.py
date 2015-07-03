# Echo client program 
import socket 


myfile = open("input.txt", "r")
inputtxt = myfile.read()


HOST = ' 140.112.149.69' # According to your server ip address 

PORT = 30023 # The same port as used by the server 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((HOST, PORT)) 
s.sendall(inputtxt) 

data = s.recv(1024) 

output = open("r03922133.txt","w")
output.write("%s" %data)
output.close()
myfile.close()

s.close() 

print 'Received:', data 


