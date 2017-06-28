# DataCommunication-StopNWait
******************************************************************************************************************************************************
AUTHOR:
******************************************************************************************************************************************************
NAME      : Gaurav Diwate
Occupation: Student at ITP department at University of Colorado Boulder.
SID       : 105755934
IDENTIKEY : gadi5945
Contact   : Email  :  Gaurav.Diwate@coorado.edu
            Phone  :  720-345-1611
*****************************************************************************************************************************************************

WELCOME!
                   
DATA COMMUNICATIONS PROGRAMMINIG ASSIGNMENT 2 FOR STOP AND WAIT PROTOCOL IMPLEMENTATION OVER UDP:

SOFTWARE VERSION :Python 2.7.10

*****************************************************************************************************************************************************
PROGRAMM FEATURES:
***************************************************************************************************************************************************** 
     
1. FILE TYPES: This programm serves the five file formats ".txt",".pdf",".jpg",".png",".mp3"(song) and ".mp4"(video). 

2. Sender "StopNWaitS" is provided with IP address, Port Number and the file which is to be sent to Receiver "StopNWaitR".

3. Receiver "StopNWait" is provided with port number. Command "bind" binds the receiver socket to the port over which it receives data from 
   sender.

4. PACKET DROP TEST FUNCTION: Once acknowledgement for SYN packet is received by sender, actual data is being transmitted. Just before sending data
   and before sending ACK packets, a packet drop function is initiated which is interpreted as "percentage packet loss(0 to 100)". Currently 
   packet loss is set to 0% on both sender and receiver sides, But this can be changed to any value to observe packet loss scenario.   
   ws.conf consists of PORT number, Root directory details and all the file types. 

5. ACK HANDLING: Sender sends out packets(packet size limitted to 1024 bytes) with alternate sequence numbers as 0 and 1 upon receiving ACK 
   packet from receiver.

6. TIMMEOUT: A timeout of 500ms is initiated which acs as RTT. If ACK packet from receiver is not received within this time period, it is assumed 
   to be lost and previous packet is resent by sender.

7. TERMINATION: Sender will send final packet "FIN" once all data packets are sent. Receiver will respond with acknowledgement packet "ACK". Once
   ACK is received by sender, it confirms successful transfer of a file. At the same time, receiver confirms completion of file transfer and receipt
   of the same.

8. FILE HANDLING: Receiver opens an empty file as "Received-filename", once SYN packet is received. Once actual data starts coming in, it is written
   in the file. Once all data is received, file gets saved to source folder.   

9. BONUS IMPLEMENTATION 1-NETWORK TERMINATION:

     i) Sender sends FIN packet afer finishing up with dta packets.
    ii) Receiver responds with ACK packet along with it's own FIN packet with sequencee number 0 and then waits for ACK from sender. Once ACK is 
        received, it closes itself and prints "CONNECTION CLOSED SUCCESSFULLY".
   iii) In case, ACK is not received, receiver retransmitts FIN packet upto 6 times and if still ACK is not received, then prints "CONNECTION
        CLOSED DUE TO UNREACHABLE NETWORK".
    iV) When sender receives ACK for it's FIN packet, a counter of 2000ms is initiated(as a WAIT state). During this time, sender is supposed to 
        receive FIN packet from receiver and reply back to receiver with acknowledgment packet. Counter is reset after this process. Now, once it 
        reaches 0, sender closes itself and prints "CONNECTION CLOSED". 

10. WAIT COUNTER: Graceful network termination is important. WAIT counter allows sender to accept and respond to connection close confirmation 
    from receiver. It is reset if receiver FIN packet is not received in time so that it can be accepted again. In the absence of wait counter,
    sender may go off without communicating with receiver. Wait counter is utilized to respond with "ACK" so that receiver can also close itself
    indicating complete, successful transmission of any file of any size.  
     
*****************************************************************************************************************************************************
FILES LIST       : This Stop and Wait protocol implementation is tested for below files.
*****************************************************************************************************************************************************
                   1. text.txt
	                 2. PDF.pdf
                   3. moon.jpg
                   4. ice.png
                   5. song.mp3
                   6. video.mp4															  
                
                   
*****************************************************************************************************************************************************
