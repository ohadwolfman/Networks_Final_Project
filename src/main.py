import socket
from scapy.all import *

IP = '127.0.0.1'
PORT = 80

def main():
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.connect((IP, PORT))

    filterWhatsApp = "tcp and port 443"  # According to official facebook: 5222, 443
    filterTelegram = "tcp and port"  # TCP on port 80, 443, or 5222
    filterFacebookMessenger = "tcp and port"  # TCP on port 3478 or 443 or 5222

    sniff(filter=filterWhatsApp)


if __name__ == '__main__':
    main()