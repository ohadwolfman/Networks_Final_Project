# Networks - Final Project
## Instance messages reference transportation analysis

### Introduction
- In this project, we based on the paper "Practical Traffic Analysis Attacks on Secure Messaging Applications"
- The paper claims that although instant message applications claim to be entirely secret, by simple statistics methods and filtering we can receive good information about the data that is transported.
- For each such group that is presented in the paper we plotted the inter-message delays and the message sizes, and we looked for unique characteristics for each group - messages, images, videos, files, and audio groups.
- We considered 2 cases:
	- The attacked user is always active in (at most) a single IM group.
	- The attacked user may be active in several IM groups simultaneously.


### Directories and files
- src directory, which includes all your code.
- resources directory: includes some sample raw data for the work (traces / pcap files etc.).
- res directory: includes the results (text files / Python pickle files).

### Dataset details and additional information
- We exported every Wireshark record to a csv files for the analyzing.
- Every csv file contains the following columns:
    - No. - the packet number 
    - Time - the timestamp of when the packet or message was captured in milliseconds
    - Source - the source IP address
    - Destination - the destination IP address
    - Protocol - the network protocol used for the communication
    - Length - the length of the packet in bytes including the headers and the data payload
    - Info:
        - 443 > 35260: This part indicates the source and destination ports of the TCP communication. "443" is the source port, and "35260" is the destination port.
        - [flags]: These are TCP flags set in the packet.
         for example [PSH, ACK] that represents "Push" for telling the receiving side to deliver the data to the application immediately, rather than buffering it.
         and in addition, ACK for "Acknowledgment" and indicates that the packet is an acknowledgment of previously received data.
        - Seq=1: It represents the sequence number of the packet.
        - Ack=360: It represents the acknowledgment number - used to inform the sender about the number of bytes it has received successfully.
        - Win=65535: It represents the number of bytes that can be sent before waiting for an acknowledgment.
        - Len=1392: It represents the length of the actual data of the TCP segment in bytes.
- The IM platform WhatsApp uses TLSv1.2 protocol which is a cryptographic protocol used to secure communications over a computer network
    - It ensures that data transmitted between the client and server is encrypted
    - It allows the client and server to verify each other's identities using digital certificates, preventing man-in-the-middle attacks
- Each SIM event, e.g., a sent image, produces a burst of MTU-sized packets in the encrypted traffic with very small inter-packet delays.

### The cleaning process:
Initially, our approach involved filtering based on a singular protocol that appeared recurrently within the dataset. However, it became evident that this method inadvertently excluded a substantial amount of communication data. As a remedy, rather than focusing on a single protocol, we chose to filter out non-relevant protocols that were conclusively not transmitting WhatsApp communication data, such as DNS and NTP, among others.

Subsequently, in an effort to further refine the dataset and eliminate noise, we evaluated the IPs from which messages were being sent. It was observed that certain messages were routed through servers not affiliated with Facebook, the parent company of WhatsApp. These unrelated servers were then filtered based on their geographical location, specifically whether they were located within Israel. Generally speaking, the majority of WhatsApp communication is relayed via Facebook's servers. If the communication isn't directed straight to WhatsApp, it's likely due to the substantial size of the transmitted data, which is then routed through a local server, typically residing in Israel as an ISP.

In addition, we implemented further IP filtering based on the median packet size and the number of packets dispatched from that address. An IP from which a substantial number of packets (greater than 1000) were dispatched was considered significant. If the median size exceeded 500, it was inferred that the transmitted packets probably contained pertinent information. Upon closer inspection, we noted that servers transmitting sizable data typically had a median packet size of around 1200, establishing 500 as a safety threshold.

To address potential anomalies or aberrations in packet sizes, we posited that if the top three largest packets (or the top 0.001% of packet lengths, whichever is smaller) are more than three times the size of the subsequent packet, it likely indicates an inadvertent error in the recording, warranting the removal of those packets.

Lastly, the filtering was further refined by examining the content detailed in the 'info' description of each packet. All packets labeled 'Len=0' were excluded since this value denotes the size of the transferred data excluding headers, leading us to deduce that these packets essentially transmitted no data. Finally, we surveyed the varying types of 'info' and, based on their descriptions and average packet sizes, made determinations on which to omit. For instance, packets described as 'Initial', which denotes the inception of a connection, or 'Client Hello', which is also devoid of pertinent data, were among those excluded.



we weren't able to identify unique characteristics for each group

### Deducing the groups an attacked user take part in using the techniques detailed in the paper:
#### When the attacked user is always active in (at most) a single IM group:

#### When the attacked user is may active in several IM groups simultaneously:

### References
- The paper: https://www.ndss-symposium.org/wp-content/uploads/2020/02/24347-paper.pdf
- The researchers GitHub repo: https://github.com/SPIN-UMass/IMProxy

### Authors
- Wolfman Ohad, https://www.linkedin.com/in/ohad-wolfman/
- Chesler Shira, https://www.linkedin.com/in/shira-chesler-4438b5222/

