import socket
from scapy.all import *

IP = '127.0.0.1'
PORT = 80

def main():
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.connect((IP, PORT))

    filterBy = "tcp"
    sniff(filter=filterBy)


if __name__ == '__main__':
    main()