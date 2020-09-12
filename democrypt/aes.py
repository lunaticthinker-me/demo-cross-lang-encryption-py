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
    iv = get_random_bytes(AES.block_size)
    aes = AES.new(self.hash, self.mode, iv)
    paddedtext = self.pkcs7_padding(plaintext) if self.mode == AES.MODE_CBC else plaintext
    encrypted = aes.encrypt(bytes(paddedtext, 'utf-8'))
    return base64.b64encode(iv + encrypted).decode('utf-8')

  def decrypt(self, ciphertext: str) -> str:
    cipher = base64.b64decode(bytes(ciphertext, 'utf-8'))
    iv = cipher[0:16]
    aes = AES.new(self.hash, self.mode, iv)
    paddedtext = aes.decrypt(cipher[16:]).decode('utf-8')
    return self.pkcs7_trimming(paddedtext) if self.mode == AES.MODE_CBC else paddedtext

  def pkcs7_padding(self, s: str) -> str:
    """
    Padding to blocksize according to PKCS #7
    calculates the number of missing chars to BLOCK_SIZE and pads with
    ord(number of missing chars)
    @see: http://www.di-mgt.com.au/cryptopad.html
    """
    s_len = len(s)
    BS = AES.block_size
    s = s + (BS - s_len % BS) * chr(BS - s_len % BS)
    return s

  def pkcs7_trimming(self, s: str) -> str:
    """
    Trimming according to PKCS #7
    @param s: string Text to unpad
    @type s: string
    @rtype: string
    """
    cut = bytes(s, 'utf-8')[-1]
    return s[0:-cut]
