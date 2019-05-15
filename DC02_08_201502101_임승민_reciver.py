import socket 
import os

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(('',9003))

file_name, addr = s.recvfrom(2000)
file_size, _ = s.recvfrom(2000)

print("file recv start from ", addr[0])
print(file_name)
print("File Name : " , file_name.decode())
print("FIle Size : " , file_size.decode())

current_size = 0

with open(file_name, 'wb') as recive_file :
    for r in range(0,int(file_size.decode()),1024):
        
        current_size += 1024
        data, _ = s.recvfrom(1024)
        recive_file.write(data)
        per = current_size / int(file_size) * 100
        if per >= 100 :
             print("current_size / total_size = " , file_size.decode(), "/" , file_size.decode() ,",", '100' ,"%")
        else:
            per = str(per)
            print("current_size / total_size = " , current_size, "/" , file_size.decode(),"," , per ,"%")
