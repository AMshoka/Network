import socket
import os


def soCKET(name,path):
    NS = socket.socket()
    host = socket.gethostname()
    port = 13766
    NS.connect((host,port))


    NS.send(str.encode( name ))
    resp =NS.recv(1002)
    print(resp.decode())
    text = NS.recv(1000)
    if text:
        file=open(path+"file"+name, "w")
        file.write(text.decode())
        file.close()
    NS.close()


name= input("file's name : ")
path= input("path : ")
soCKET(name,path)




