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


def convert_plain_to_binary_splitted(plain):
    plain_splitted = utils.string_to_array(plain, 8)
    plain_binary_splitted = []
    for p in plain_splitted:
        plain_binary_splitted.append(utils.string_to_binary(p))
    utils.debugLine()
    utils.debug('plain text           ', plain)
    utils.debug('plain splitted       ', plain_splitted)
    utils.debug('plain splitted binary', plain_binary_splitted)
    return plain_binary_splitted


def convert_key_to_binary(key):
    key_binary = utils.string_to_binary(key)
    utils.debugLine()
    utils.debug('key text  ', key)
    utils.debug('key binary', key_binary, 7)
    return key_binary


def convert_iv_to_binary(iv):
    iv_binary = utils.string_to_binary(iv)
    utils.debugLine()
    utils.debug('iv text  ', iv)
    utils.debug('iv binary', iv_binary, 7)
    return iv_binary


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


def convert_cipher_temp_to_hex(cipher_binary_temp):
    cipher_binary_temp_splitted = utils.string_to_array(cipher_binary_temp, 8)
    cipher_temp = ''
    for c in cipher_binary_temp_splitted:
        cipher_temp += utils.binary_to_hex(c)
    utils.debugLine()
    utils.debug('cipher temp binary', cipher_binary_temp, 8)
    utils.debug('cipher temp', cipher_temp)
    return cipher_temp


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

    return permute(r[16] + l[16], tables.IP_INV)


def start(mode, plain, key):
    # plain
    # mode = raw_input('Mode (Encrypt / Decrypt) : ').lower()
    # plain = raw_input('Enter input to ' + mode + ' : ')
    # plain = 'Beberapa kota yang sudah mulai membangun Smart City diantaranya adalah Surabaya, Jakarta, Bandung dan Tangerang'
    # plain = 'a24800279f63f313faed7865e3ac1a6267872c2012b35803a4cc2d173b94cda6b3c82c4a83a2cce60914913318b1a5cec318a7ded66805eb484cb98275364939a3a0427515f23b3a7416049dd0b8ee8ab72911828dbfdb2fe78223fb1e67a4d5de0bf510bd98507124ab7c3d2d6c7790'

    if mode == 'decrypt':
        plain = plain.decode('hex')
    plain_binary_splitted = convert_plain_to_binary_splitted(plain)
    block = len(plain_binary_splitted)

    # key
    key_binary = convert_key_to_binary(key)

    # init vector
    iv = 'QWERTYUI'
    iv_binary = convert_iv_to_binary(iv)

    # C, D, K
    c, d = generate_cd(key_binary)
    k = generate_k(c, d)

    # blocks loop
    plain_binary_splitted = [iv_binary] + plain_binary_splitted
    cipher_binary_splitted = [iv_binary]
    for i in range(block):
        # des
        if mode == 'decrypt':
            temp = plain_binary_splitted[i]
        elif mode == 'encrypt':
            temp = cipher_binary_splitted[i]

        des_k = des(k, temp)
        cipher_binary_temp = utils.xor(plain_binary_splitted[i + 1], des_k)
        cipher_binary_splitted.append(cipher_binary_temp)
    plain_binary_splitted.remove(iv_binary)
    cipher_binary_splitted.remove(iv_binary)

    # cipher
    cipher_binary = ''
    cipher_hex = ''
    for c in cipher_binary_splitted:
        cipher_binary += c
        cipher_hex += convert_cipher_temp_to_hex(c)
    cipher = cipher_hex.decode('hex')
    utils.debugLine()
    utils.debug('cipher bin ', cipher_binary, 8)
    utils.debug('cipher hex ', cipher_hex)
    utils.debug('cipher text', cipher)

    if mode == 'encrypt':
        return cipher_hex
    else:
        return cipher


def encrypt(text, key):
    return start('encrypt', text, key)


def decrypt(hex, key):
    return start('decrypt', hex, key)
