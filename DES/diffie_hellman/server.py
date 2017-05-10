import select
import socket
import sys

import des_cfb
import utils

def diffie_hellman():
    print "get q and a from client"
    q = utils.int_recv(client_socket)
    a = utils.int_recv(client_socket)
    utils.forceDebug("q", q)
    utils.forceDebug("a", a)

    print "set xb, compute yb"
    xb = 233
    yb = pow(a, xb, q)
    utils.forceDebug("xb", xb)
    utils.forceDebug("yb", yb)

    print "get ya, send yb"
    ya = utils.int_recv(client_socket)
    utils.int_send(client_socket,yb)
    utils.forceDebug("ya", ya)

    print "compute kab(key)"
    kab = pow(ya, xb, q)
    return str(kab)

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

                key = diffie_hellman()
                utils.forceDebug("key", key)

                cipher = sock.recv(4096)
                plain = des_cfb.decrypt(cipher, key)

                utils.forceDebug('cipher', cipher, 16)
                utils.forceDebug('plain', plain)
                utils.forceDebugLine()

                sock.close()
                input_socket.remove(sock)


except KeyboardInterrupt:
    server_socket.close()
    sys.exit(0)
