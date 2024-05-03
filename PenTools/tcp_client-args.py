import socket
import argparse

# TODO
#Convert to Args
#Add Stdin and out to pass messages
#Add Args for Host and Port at command run

parser = argparse.ArgumentParser()
parser.add_argument("host", help="python tcp_client-args.py 0.0.0.0 9998")
parser.add_argument("port", help="python tcp_client-args.py 0.0.0.0 9998")
args = parser.parse_args()

HOST = args.host
PORT = int(args.port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.send(b'GET / HTTP/1.1\r\nHost: ABCDEFG\r\n\r\n')
response = client.recv(4096)
print(response.decode('utf-8'))

client.close()

