import socket
from datetime import datetime
from http import HTTPStatus

HOST = "localhost"
PORT = 40404

http_response = (
    f"HTTP/1.0 200 OK\r\n"
    f"Server: otusdemo\r\n"
    f"Date: Sat, 01 Jan 2023 10:00:00 GMT\r\n"
    f"Content-Type: text/html; charset=UTF-8\r\n"
    f"\r\n"
)

end_of_stream = '\r\n\r\n'


def handle_client(connection, clientAddress):
    client_data = ''
    with connection:
        while True:
            data = connection.recv(1024)
            print("Received:", data)
            if not data:
                break
            client_data += data.decode()
            if end_of_stream in client_data:
                break

        server_utc_time_now = str(datetime.utcnow())
        client_lines = client_data.splitlines()
        (method, query, protocol) = client_lines[0].split()
        url_parts = query.split('?')
        status = HTTPStatus.OK
        if len(url_parts) > 1:
            for query_param in url_parts[1].split('&'):
                if query_param.startswith("status="):
                    status = parse_status(query_param.split('=')[1])

        connection.send(f"HTTP/1.0 {status} {status.phrase}\r\n"
                        f"Server: otusdemo\r\n"
                        f"Date: Sat, 01 Jan 2023 10:00:00 GMT\r\n"
                        f"Content-Type: text/html; charset=UTF-8\r\n"
                        f"\r\n"
                        f"Request Method: {method}\r\n"
                        f"Request Source: {clientAddress}\r\n"
                        f"Response Status: {status} {status.phrase}\r\n".encode() +
                        "\r\n".join(client_lines[1:]).encode() +
                        f"\r\n".encode())


def parse_status(status_code):
    try:
        return HTTPStatus(int(status_code))
    except ValueError:
        return HTTPStatus.INTERNAL_SERVER_ERROR


def run_server():
    with socket.socket() as serverSocket:
        serverSocket.bind((HOST, PORT))

        print(f"Running server on {HOST}:{PORT}...")
        serverSocket.listen()

        while True:
            (clientConnection, clientAddress) = serverSocket.accept()
            handle_client(clientConnection, clientAddress)
            print(f"Sent data to {clientAddress}")


if __name__ == "__main__":
    run_server()
