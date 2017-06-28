import socket
import sys
import os
from random import randint


sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
x=sys.argv[1]
y=sys.argv[2]
Y=y.split(':')
Y1=Y[0]
Y2=int(Y[1])

Filesiz=os.path.getsize(x)
print("FILE SIZE:", Filesiz)
print()
#Filesiz=int(Filesiz)
Pkts=(Filesiz//1024)
Pkts1=int(Pkts)
if Pkts1<<(Pkts):
    Pkts1=Pkts1+1
    print("NO. OF PACKETS:",Pkts1)
print()
sock.sendto(str(Pkts1), (Y1,Y2))
print("SENT TO RECEIVER")

SN=0
L=0
CP=1                                                                             # Sending SYN Packet
Packet=str(SN)+"|||"+str("SYN")+"|||"+str(x)
Packet=Packet.encode()
sock.sendto(Packet, (Y1,Y2))
data, address=sock.recvfrom(1024)
if data:    
    text=data.decode()
    print("RECEIVED ACK:"+' '+text[0]+' '+"FROM RECEIVER")
    print()
SN=SN+1
    

fh=open(x,'rb')
m=0

while (CP<=Pkts1):  
    ploss=randint(0,100)                                                             #Packet drop function                                 
    #print("PACKET DROP")
    if ploss>0:              
        sock.settimeout(0.5)                                                     # Timeout Function   
        try:                                                                     # Sending Data Packets
            fh.seek(m)
            Text=fh.read(1024)
            #Text=Text.encode()
            Packet= str(SN)+"|||"+str("Data")+"|||"+str(Text)
            #Packet1=Packet.encode()
            sock.sendto(Packet, (Y1,Y2))
            print()
            print("PACKET"+' '+str(CP)+' '+"IS BEING SENT")
            while True:
                info, address=sock.recvfrom(1024)
                if info:
                    text=info.decode()
                    print("RECEIVED ACK:"+' '+str(CP)+' '+"FROM RECEIVER")
                    break 
            m=m+1024
            if SN>L:
                SN=L
            else:
                SN=SN+1
            #Pkts1=Pkts+1
            CP=CP+1
        except:
            print("ACK NOT RECEIVED WITHIN TIMEOUT PERIOD")
              
fh.close()
Packet=str(SN)+"|||"+str("FIN")                                                  # Sending Final Packet
Packet=Packet.encode()
sock.sendto(Packet,(Y1,Y2))
print()
print("FINAL PACKET IS SENT")
print()
data, address=sock.recvfrom(1024)
ACK=data.decode()
print("ACK:"+' '+ACK[1:7]+' '+"FOR FINAL PACKET IS RECEIVED")
print()
print(sys.argv[1]+' '+"IS SUCCESSFULLY SENT TO"+' '+str(Y1)+":"+''+str(Y2))

sock.close()  