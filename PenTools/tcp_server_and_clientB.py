import socket
import threading

IP = '0.0.0.0'

SND_PORT = 9999
RCV_PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, RCV_PORT))
    server.listen(5)
    print(f'[*] Listening on {IP}:{RCV_PORT}')

    client, address = server.accept()
    print(f'[*] Accepted Connection from {address[0]}:{address[1]}')
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
    msg = threading.Thread(target=message, args=(msg,))
    msg.start()


def handle_client(client_socket):
    with client_socket as sock:
        while True:
            request = sock.recv(1024)
            print(f'[*] Recieved: {request.decode("utf-8")}')
            sock.send(b'ACK')
            if request.decode() == "quit":
                print('Closing Server')
                break

def message():   
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP,SND_PORT))
    while True:
        cmd = input()
        client.send(cmd.encode('utf-8'))
        response = client.recv(4096)
        print(response.decode('utf-8'))
        if 'quit' == cmd.rstrip():
            break


if __name__ == '__main__':
    main()
