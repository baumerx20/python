import socket
import argparse
import sys


# TODO
#Add Stdin and out to pass messages
#Add Args for Host and Port at command run

parser = argparse.ArgumentParser()
parser.add_argument("host", help="python tcp_client-args.py 0.0.0.0 9998")
parser.add_argument("port", help="python tcp_client-args.py 0.0.0.0 9998")
args = parser.parse_args()

HOST = args.host
PORT = int(args.port)


def message():   
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST,PORT))
    while True:
        cmd = input()
        client.send(cmd.encode('utf-8'))
        response = client.recv(4096)
        print(response.decode('utf-8'))
        if 'quit' == cmd.rstrip():
            break
        
if __name__ == '__main__':
    message()


