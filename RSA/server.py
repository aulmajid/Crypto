import select
import socket
import sys
from fractions import gcd

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
                p = 12131072439211271897323671531612440428472427633701410925634549312301964373042085619324197365322416866541017057361365214171711713797974299334871062829803541
                q = 12027524255478748885956220793734512128733387803682075433653899983955179850988797899869146900809131611153346817050832096022160146366346391812470987105415233
                n = p * q
                phi = (p - 1) * (q - 1) / gcd(p - 1, q - 1)

                e = 65537
                if (e > 1 and e < phi and gcd(e, phi) == 1):
                    print 'e memenuhi syarat'
                else:
                    print 'e tidak memenuhi syarat'

                d = 89489425009274444368228545921773093919669586065884257445497854456487674839629818390934941973262879616797970608917283679875499331574161113854088813275488110588247193077582527278437906504015680623423550067240042466665654232383502922215493623289472138866445818789127946123407807725702626644091036502372545139713
                ed = (e * d) % phi
                if ( ed == 1):
                    print 'd memenuhi syarat'
                else:
                    print 'd tidak memenuhi syarat'

                print 'p : ' + str(p)
                print 'q : ' + str(q)
                print 'n : ' + str(n)
                print 'e : ' + str(e)
                print 'd : ' + str(d)

                utils.int_send(sock, n)
                utils.int_send(sock, e)

                cipher_ascii = utils.int_recv(sock)
                print 'cipher ascii : ' + str(cipher_ascii)

                plain_ascii = pow(cipher_ascii, d, n)
                print 'plain ascii : ' + str(plain_ascii)

                plain = utils.ascii_to_string(plain_ascii)
                print 'plain : ' + plain


                sock.close()
                input_socket.remove(sock)


except KeyboardInterrupt:
    server_socket.close()
    sys.exit(0)
