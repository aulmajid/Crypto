import select
import socket
import sys

import rsa
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
                sock.recv(4)

                p = 353
                q = 17
                n, m, e, d = rsa.generate_value(p, q)
                print 'p : ' + str(p)
                print 'q : ' + str(q)
                print 'n : ' + str(n)
                print 'm : ' + str(m)
                print 'e : ' + str(e)
                print 'd : ' + str(d)
                utils.int_send(sock, n)
                utils.int_send(sock, e)

                length = utils.int_recv(sock)
                cipher_ascii = []
                for i in range(length):
                    cipher_ascii.append(utils.int_recv(sock))
                print 'cipher ascii : ' + utils.array_to_string(cipher_ascii)

                plain_ascii_array, plain_ascii = rsa.decrypt(cipher_ascii, d, n)
                print 'plain ascii : ' + plain_ascii

                plain = utils.ascii_array_to_string(plain_ascii_array)
                print 'plain : ' + plain

                print ' '

                sock.close()
                input_socket.remove(sock)


except KeyboardInterrupt:
    server_socket.close()
    sys.exit(0)
