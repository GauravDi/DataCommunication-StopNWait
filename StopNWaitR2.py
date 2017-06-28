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
        print("ACK:0 IS SENT")
    else:
        print("SYN PACKET DELIVERY FAILED")
    print()
    print("DATA TRANSFER INITIATED")


while P<=pkts1:
    i=randint(0,100)
    if (i>0):                                                            #Packet drop function
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
print()
print("FILE TRANSFER COMPLETE")
fh.close()
print()
print("FILE:"+' '+FILENAME+' '+"IS RECEIVED")

        
inf, address=sock.recvfrom(a)    
if inf:
    text=inf.decode()
    text1=text.split('|||')
    if text1[1]=="FIN":
        ACK=text1[0]+"ACKFIN"
        sock.sendto(ACK, address)
        FIN="0"+"RCVFIN"
        sock.sendto(FIN,address)
        l=randint(0,100)
        data,address=sock.recvfrom(a)
        if data:
            text=data.decode()
            if l>0:
                if text=="FINACK":
                    print()
                    print("ACK FOR FIN PACKET"+' '+text+' '+"IS RECEIVED")
                    print()
                    print("CONNECTION CLOSED SUCCESSFULLY")
            else:
                Q=0
                while Q<6:
                    FIN="0"+"RCVFIN"
                    sock.sendto(FIN,address)
                    print()
                    print("FINAL PACKET-RETRANSMITTED")
                    Q=Q+1
                print()
                print("CONNECTION CLOSED DUE TO UNREACHABLE NETWORK")
sock.close()