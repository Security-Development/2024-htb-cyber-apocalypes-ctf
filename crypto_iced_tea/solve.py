from Crypto.Util.number import bytes_to_long as b2l, long_to_bytes as l2b

block_size = 64
key = "850c1413787c389e0b34437a6828a1b2"
key_bytes = bytes.fromhex(key) # get key
delta = 0x9e3779b9

key = [b2l(key_bytes[i:i+block_size//16]) for i in range(0, len(key_bytes), block_size//16)]

cipher = "b36c62d96d9daaa90634242e1e6c76556d020de35f7a3b248ed71351cc3f3da97d4d8fd0ebc5c06a655eb57f2b250dcb2b39c8b2000297f635ce4a44110ec66596c50624d6ab582b2fd92228a21ad9eece4729e589aba644393f57736a0b870308ff00d778214f238056b8cf5721a843"

def _xor(a, b):
    return b''.join(bytes([_a ^ _b]) for _a, _b in zip(a, b))

from Crypto.Util.Padding import unpad

def encrypt(self, msg):
    msg = pad(msg, self.BLOCK_SIZE//8)
    blocks = [msg[i:i+self.BLOCK_SIZE//8] for i in range(0, len(msg), self.BLOCK_SIZE//8)]
    
    ct = b''

    for pt in blocks:
        ct += self.encrypt_block(pt)

def encrypt_block(self, msg):
        m0 = b2l(msg[:4])
        m1 = b2l(msg[4:])
        K = self.KEY
        msk = (1 << (self.BLOCK_SIZE//2)) - 1

        s = 0
        for i in range(32):
            s += self.DELTA
            m0 += ((m1 << 4) + K[0]) ^ (m1 + s) ^ ((m1 >> 5) + K[1])
            m0 &= msk
            m1 += ((m0 << 4) + K[2]) ^ (m0 + s) ^ ((m0 >> 5) + K[3])
            m1 &= msk
        
        m = ((m0 << (self.BLOCK_SIZE//2)) + m1) & ((1 << self.BLOCK_SIZE) - 1) # m = m0 || m1

        return l2b(m)

def decrypt(ct):
    blocks = [ct[i:i+block_size//8] for i in range(0, len(ct), block_size//8)]
    
    pt = b''

    for ct_block in blocks:
        pt += decrypt_block(ct_block)

    return unpad(pt, block_size//8)


def decrypt_block(ct_block):
    m = b2l(ct_block)
    K = key
    msk = (1 << (block_size//2)) - 1

    m1 = m & msk
    m0 = m >> (block_size//2)

    s = delta * 32

    for i in reversed(range(32)):
        m1 -= ((m0 << 4) + K[2]) ^ (m0 + s) ^ ((m0 >> 5) + K[3])
        m1 &= msk

        m0 -= ((m1 << 4) + K[0]) ^ (m1 + s) ^ ((m1 >> 5) + K[1])
        m0 &= msk

        s -= delta

    return l2b(m0) + l2b(m1)




print(decrypt(bytes.fromhex(cipher)))