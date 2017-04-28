import socket

import des_cfb
import utils

def diffie_hellman():
    print "set q and a, send to server"
    q = 200
    a = 3
    utils.forceDebug("q",q)
    utils.forceDebug("a",a)
    utils.int_send(client_socket,q)
    utils.int_send(client_socket,a)

    print "set xa, compute ya"
    xa = 97
    ya = pow(a,xa,q)
    utils.forceDebug("xa",xa)
    utils.forceDebug("ya",ya)

    print "send ya, get yb"
    utils.int_send(client_socket,ya)
    yb = utils.int_recv(client_socket)
    utils.forceDebug("yb",yb)

    print "compute kab(key)"
    kab = pow(yb,xa,q)
    return str(kab)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.43.104', 12346)
client_socket.connect(server_address)

key = diffie_hellman()
utils.forceDebug("key",key)

plain = 'Beberapa kota yang sudah mulai membangun Smart City diantaranya adalah Surabaya, Jakarta, Bandung dan Tangerang'
cipher = des_cfb.encrypt(plain, key)

utils.forceDebug('plain ', plain)
utils.forceDebug('cipher', cipher, 16)

client_socket.send(cipher)
