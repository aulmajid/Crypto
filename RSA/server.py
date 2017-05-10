import select
import socket
import sys

import utils

server_address = ('localhost', 12346)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(server_address)
server_socket.listen(5)

input_socket = [server_socket]

try:
    while True:
        read_ready, write_ready, exception = select.select(input_socket, [], [])

        for sock in read_ready:
            if sock == server_socket:
                client_socket, client_address = server_socket.accept()
                input_socket.append(client_socket)
            else:
                # receive data from client
                n = utils.int_recv(sock)
                e = utils.int_recv(sock)
                print 'n : ' + str(n)
                print 'e : ' + str(e)

                sock.close()
                input_socket.remove(sock)


except KeyboardInterrupt:
    server_socket.close()
    sys.exit(0)
