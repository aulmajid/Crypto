import numpy as np
import fractions as fr
import utils


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def generate_value(p, q):
    n = p * q
    m = (p - 1) * (q - 1)

    while True:
        e = np.random.randint(1, m)
        if fr.gcd(e, m) == 1:
            break

    d = modinv(e, m)

    return n, m, e, d


def encrypt(plain_ascii_array, e, n):
    cipher_ascii_array = []
    for ascii in plain_ascii_array:
        cipher_ascii_array.append(pow(ascii, e, n))
    return cipher_ascii_array, utils.array_to_string(cipher_ascii_array)


def decrypt(cipher_ascii_array, d, n):
    plain_ascii_array = []
    for ascii in cipher_ascii_array:
        plain_ascii_array.append(pow(ascii, d, n))
    return plain_ascii_array, utils.array_to_string(plain_ascii_array)
