import socket 
import os

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

host = '192.168.137.151' 
port= 9003

name = input("Input your file name : ")
s.sendto(name.encode(),(host,int(port)))

print("File Transmit Start") 

file_size = str(os.path.getsize(name))
s.sendto(file_size.encode(),(host,int(port)))


with open(name, 'rb') as file:
    current_size = 0
    data = file.read(1024)
    while data:
        s.sendto(data,(host,int(port)))
        current_size += 1024
        per = current_size / int(file_size) * 100
        data = file.read(1024)
        if per >= 100 :
            print("current_size / total_size = " , file_size, "/" , file_size ,",", '100' ,"%")
       
        else :
            per = str(per)
            print("current_size / total_size = " , current_size, "/" , file_size ,",", per ,"%")

print("OK")
print("file_send_end") 

