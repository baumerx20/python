import socket
import argparse

def server(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', port))
        s.listen(1)
        print(f"Listening on port {port}...")
        conn, addr = s.accept()
        with conn:
            print(f"Connected to {addr[0]}:{addr[1]}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(data.decode(), end='')

def client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(f"Connected to {host}:{port}")
        while True:
            message = input()
            s.sendall(message.encode())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Netcat Replacement")
    parser.add_argument('-l', '--listen', dest='listen', action='store_true', help="Listen mode")
    parser.add_argument('-p', '--port', dest='port', type=int, help="Port number", default=12345)
    parser.add_argument('host', nargs='?', help="Host to connect to (for client mode)")
    args = parser.parse_args()

    if args.listen:
        server(args.port)
    elif args.host:
        client(args.host, args.port)
    else:
        print("Either specify host to connect or use listen mode.")