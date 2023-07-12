import socket

# msgFromClient=ans
bytesToSend=msgFromClient.encode('utf-8')
serverAddress = ("192.168.153.116" , 2222)
bufferSize = 1024
UDPClient = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
UDPClient.sendto(bytesToSend, serverAddress)
data,address=UDPClient.recvfrom(bufferSize)
data = data.decode("utf-8")
print("data from server " , data)
print("Server IP Address: ", address[0])
print("Server Port: ", address[1])
