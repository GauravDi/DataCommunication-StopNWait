import socket
import sys
from random import randint

sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
a=sys.argv[1]
a=int(a)
addr=('',a)
sock.bind(addr)
P=1

data, address=sock.recvfrom(a)
if data:
    pkts=data.decode()
    pkts1=int(pkts)
    #pkts=int(pkts)
    print("NO. of PACKETS:",pkts1)

data, address = sock.recvfrom(a)                                 # Sending ACK0
if data:
    text=data.decode()
    text=text.split('|||')
    print()
    print("SEQUENCE NUMBER:", text[0])
    fh=open("Received-"+text[2],'wb')
    print()
    FILENAME=text[2]
    print("FILE NAME:", text[2])
    #text[0]=text[0].encode()
    if text[1]=="SYN":
        ACK=str(text[0])+"|||"+"ACK"
        ACK=ACK.encode()
        sock.sendto(ACK,(address))
        print()
        print("ACK:"+' '+text[0]+' '+"FOR SYN PACKET IS SENT")
    else:
        print("SYN PACKET DELIVERY FAILED")
    print()
    print("BEGIN RECEIVING:"+' '+text[2])


while P<=pkts1:
    ploss=randint(0,100)
    if (ploss>0):                                                            #Packet drop function
        info, address=sock.recvfrom(a)
        if info:                                                         # Receiving Data Packets and sending ACK's
            #text=info.decode()
            info=str(info).split('|||')
            print()
            print("SEQ NUMBER:",info[0])
            #text[2]=text[2].decode()
            fh.write(info[2])
            ACK=str(info[0])+"|||"+"ACK"
            ACK=ACK.encode()
            sock.sendto(ACK, address)
            print("ACK"+' '+str(P)+' '+"IS SENT TO SENDER")
            P=P+1

        
inf, address=sock.recvfrom(a)    
if inf:
    text=inf.decode()
    text1=text.split('|||')
    if text1[1]=="FIN":
        ACK=text1[0]+"ACKFIN"
        sock.sendto(ACK, address)
print()
print("RECEIVED FIN PACKET, ACK IS SENT")
fh.close()
print()
print("FILE:"+' '+FILENAME+' '+"IS RECEIVED")

sock.close()
