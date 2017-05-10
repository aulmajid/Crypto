def string_to_ascii(string):
    ascii = ''
    for x in string:
        ascii += str(ord(x)).zfill(3)
    return int(ascii)


def ascii_to_string(ascii):
    ascii = str(ascii)
    length = len(ascii)
    length = length + 3 - length % 3
    ascii = ascii.zfill(length)

    string = ''
    for i in range(0,length,3):
        string+= unichr(int(ascii[i:i+3]))
    return string


def string_to_array(text, length):
    texts = []
    for i in range(0, len(text), length):
        texts.append(text[i:i + length])
    return texts

def int_send(socket, value):
    socket.send(str(value) + '.')

def int_recv(socket):
    buf = ""
    while '.' not in buf:
        buf += socket.recv(1)
    num = int(buf[:-1])
    return num
