import socket

import des_cfb
import utils

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12346)
client_socket.connect(server_address)

plain = 'Beberapa kota yang sudah mulai membangun Smart City diantaranya adalah Surabaya, Jakarta, Bandung dan Tangerang'
cipher = des_cfb.encrypt(plain)

utils.forceDebug('plain ', plain)
utils.forceDebug('cipher', cipher, 16)

client_socket.send(cipher)
