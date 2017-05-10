import socket

import utils

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12346)
client_socket.connect(server_address)

client_socket.send('init')

n = utils.int_recv(client_socket)
e = utils.int_recv(client_socket)
print 'n : ' + str(n)
print 'e : ' + str(e)

plain = 'attack on titan'
print 'plain : ' + plain

plain_ascii = utils.string_to_ascii(plain)
plain_ascii = utils.string_to_ascii(plain)
print 'plain ascii : ' + str(plain_ascii)

cipher_ascii = pow(plain_ascii, e, n)
print 'cipher ascii : ' + str(cipher_ascii)

utils.int_send(client_socket, cipher_ascii)
