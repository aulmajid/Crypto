import socket

import rsa
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

plain_ascii = utils.string_to_ascii_array(plain)
print 'plain ascii : ' + utils.array_to_string(plain_ascii)
utils.int_send(client_socket, len(plain_ascii))

cipher_ascii_array, cipher_ascii = rsa.encrypt(plain_ascii, e, n)
print 'cipher ascii : ' + cipher_ascii

for ascii in cipher_ascii_array:
    utils.int_send(client_socket, ascii)
