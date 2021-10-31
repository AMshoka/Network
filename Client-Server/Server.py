import socket
import os
import sys

i=0
j=10
while i<j:
    file=open(str(i+1)+".txt","w")
    file.write("file"+str(i+1))
    i=i+1
    file.close()


NS= socket.socket()
host = socket.gethostname()
port = 13766
NS.bind((host, port))
NS.listen(5)
while True:
    client, adr = NS.accept()

    print('connect', adr )
    data=client.recv(1000)
    if os.path.exists(data):

        client.send(str.encode("200 OK"));
        file=open(data,"r")
        content=file.read()
        client.send(str.encode(content))
    else:
        client.send(str.encode("404 NOT FOUND"))

client.close()