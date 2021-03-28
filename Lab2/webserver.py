#import socket module

from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket

#Fill in start
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
#Fill in end

while True:

    #Establish the connection

    print  ("Ready to serve. . .")

    connectionSocket, addr = serverSocket.accept()

    try:

        message = connectionSocket.recv(1024)
        message.decode()
        filename = message.split()[1]
        f= open(filename[1:])
        outputdata= f.read()

        message0 = "\nHTTP\1.1 2000 OK \n"
        connectionSocket.send(message0.encode())
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()

    except IOError:
        message1 = "\nHTTP\1.1 404 Not Found \n"
        print("Inside Exception")
        connectionSocket.send(message1.encode())

        connectionSocket.close


serverSocket.close()
