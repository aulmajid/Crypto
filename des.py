import tables
import utils


def permute(binary, table):
    permuted = ''
    length = len(table)
    for i in range(length):
        permuted += binary[table[i] - 1]
    return permuted


def sbox(binary):
    b = ''
    for i in range(0, len(binary), 6):
        x = int(binary[i] + binary[i + 5], 2)
        y = int(binary[i + 1:i + 5], 2)
        utils.debugLine()
        utils.debug('x', x)
        utils.debug('y', y)
        utils.debug('SBOX', utils.int_to_binary(tables.SBOX[i / 6][x][y]))
        b += utils.int_to_binary(tables.SBOX[i / 6][x][y])
    return b


def generate_plain_binary_splitted(plain):
    plain_splitted = utils.string_to_array(plain, 8)
    plain_binary_splitted = []
    for p in plain_splitted:
        plain_binary_splitted.append(utils.string_to_binary(p))
    utils.debugLine()
    utils.debug('plain text', [plain])
    utils.debug('plain splitted', plain_splitted)
    utils.debug('plain splitted binary', plain_binary_splitted)
    return plain_binary_splitted


def generate_key_binary(key):
    key_binary = utils.string_to_binary(key)
    utils.debugLine()
    utils.debug('key', key)
    utils.debug('key binary', key_binary, 7)
    return key_binary


def generate_cd(key_binary):
    cd0 = permute(key_binary, tables.PC1)
    c = [cd0[:len(tables.PC1) / 2]]
    d = [cd0[len(tables.PC1) / 2:]]
    utils.debugLine()
    utils.debug('CD0', cd0, 7)
    for i in range(16):
        c.append(utils.left_shift(c[i], tables.LEFT_SHIFT[i]))
        d.append(utils.left_shift(d[i], tables.LEFT_SHIFT[i]))
        utils.debug('CD' + str(i + 1), c[i + 1] + d[i + 1], 7)

    return c, d


def generate_k(c, d):
    utils.debugLine()
    k = ['']
    for i in range(16):
        k.append(permute(c[i + 1] + d[i + 1], tables.PC2))
        utils.debug('K' + str(i + 1), k[i + 1], 6)
    return k


def generate_lr0(plain_temp_binary_splitted):
    lr0 = permute(plain_temp_binary_splitted, tables.IP)
    l = [lr0[:len(tables.IP) / 2]]
    r = [lr0[len(tables.IP) / 2:]]
    utils.debugLine()
    utils.debug('L0', l[0], 8)
    utils.debug('R0', r[0], 8)
    return l, r


def generate_cipher_temp(cipher_temp_binary):
    cipher_temp_binary = permute(cipher_temp_binary, tables.IP_INV)
    cipher_temp_binary_splitted = utils.string_to_array(cipher_temp_binary, 8)
    cipher_temp = ''
    for c in cipher_temp_binary_splitted:
        cipher_temp += utils.binary_to_hex(c)
    utils.debugLine()
    utils.debug('cipher temp binary', cipher_temp_binary, 8)
    utils.debug('cipher temp', cipher_temp)
    return cipher_temp


def generate_cipher(cipher_splitted):
    cipher = ''
    for c in cipher_splitted:
        cipher += c
    utils.debugLine()
    utils.debug('chiper splitted', cipher_splitted)
    utils.debug('cipher', cipher)
    return cipher


def des(k, binary):
    # L0, R0
    l, r = generate_lr0(binary)

    # core
    er = []
    a = ['']
    b = ['']
    pb = ['']
    for j in range(16):
        er.append(permute(r[j], tables.EXPANSION))
        a.append(utils.xor(er[j], k[j + 1]))
        b.append(sbox(a[j + 1]))
        pb.append(permute(b[j + 1], tables.PBOX))
        r.append(utils.xor(l[j], pb[j + 1]))
        l.append(r[j])
        utils.debugLine()
        utils.debug('ER' + str(j), er[j], 6)
        utils.debug('A' + str(j + 1), a[j + 1], 6)
        utils.debug('B' + str(j + 1), b[j + 1], 4)
        utils.debug('PB' + str(j + 1), pb[j + 1], 8)
        utils.debug('R' + str(j + 1), r[j + 1], 8)
        utils.debug('L' + str(j + 1), l[j + 1], 8)

    return r[16] + l[16]


def start():
    # plain text
    with open('input.txt', 'rb') as f:
        plain = f.read()
    plain_binary_splitted = generate_plain_binary_splitted(plain)
    block = len(plain_binary_splitted)

    # key
    key = '12345678'
    key_binary = generate_key_binary(key)

    # C, D, K
    c, d = generate_cd(key_binary)
    k = generate_k(c, d)

    # blocks loop
    cipher_splitted = []
    for i in range(block):
        # des
        cipher_temp_binary = des(k, plain_binary_splitted[i])

        # cipher temp
        cipher_temp = generate_cipher_temp(cipher_temp_binary)
        cipher_splitted.append(cipher_temp)

    # cipher
    cipher = generate_cipher(cipher_splitted)
    with open('output.txt', 'wb') as f:
        f.write(cipher)


utils.enableDebug = True
start()
