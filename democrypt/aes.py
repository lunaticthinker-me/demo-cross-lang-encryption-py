from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64


class AesCrypt:

  def __init__(self, hash: str, mode: int = AES.MODE_CFB) -> str:
    if (len(hash) != 16 and len(hash) != 24 and len(hash) != 32):
      raise Exception('hash length must be 16 or 24 or 32')

    self.hash = bytes(hash, 'utf-8')
    self.mode = mode

  def encrypt(self, plaintext: str) -> str:
    return self.encrypt_bytes(bytes(plaintext, 'utf-8')).decode('utf-8')

  def encrypt_bytes(self, plaintext: bytes) -> bytes:
    iv = get_random_bytes(AES.block_size)
    aes = AES.new(self.hash, self.mode, iv)
    paddedtext = self.pkcs7_padding(plaintext) if self.mode == AES.MODE_CBC else plaintext
    return base64.b64encode(iv + aes.encrypt(paddedtext))

  def decrypt(self, ciphertext: str) -> str:
    return self.decrypt_bytes(bytes(ciphertext, encoding='utf-8')).decode('utf-8')

  def decrypt_bytes(self, ciphertext: bytes) -> bytes:
    ciphertext = base64.b64decode(ciphertext)
    iv = ciphertext[0:16]
    aes = AES.new(self.hash, self.mode, iv)
    paddedtext = aes.decrypt(ciphertext[16:])
    return self.pkcs7_trimming(paddedtext) if self.mode == AES.MODE_CBC else paddedtext

  def pkcs7_padding(self, s: bytes) -> bytes:
    """
    Padding to blocksize according to PKCS #7
    calculates the number of missing chars to BLOCK_SIZE and pads with
    ord(number of missing chars)
    @see: http://www.di-mgt.com.au/cryptopad.html
    """
    s_len = len(s)
    BS = AES.block_size
    # s = s + (BS - s_len % BS) * chr(BS - s_len % BS)

    ss = bytearray(s)
    size = BS - s_len % BS
    for i in range(size):
      ss.append(size)
    return bytes(ss)

  def pkcs7_trimming(self, s: bytes) -> bytes:
    """
    Trimming according to PKCS #7
    @param s: string Text to unpad
    @type s: string
    @rtype: string
    """
    return s[0:-s[-1]]
