from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5
from Crypto.Hash import SHA1
from Crypto import Random
import base64

class RsaCrypt:

  def __init__(self, private: str, public: str, padding=PKCS1_v1_5):
    self.padding = padding
    self.private_key = self.padding.new(RSA.importKey(private))
    self.public_key = self.padding.new(RSA.importKey(public))

  def decrypt(self, ciphertext: str) -> str:
    return self.decrypt_bytes(bytes(ciphertext, encoding='utf-8')).decode('utf-8')

  def decrypt_bytes(self, ciphertext: bytes) -> bytes:
    if self.padding == PKCS1_v1_5:
      # # with digest
      # ciphertext = base64.b64decode(ciphertext)
      # dsize = SHA1.digest_size
      # sentinel = Random.new().read(15 + dsize)
      # message = self.private_key.decrypt(ciphertext, sentinel)
      # digest = SHA1.new(message[:-dsize]).digest()
      # if digest == message[-dsize:]:
      #   return message[:-dsize]
      # else:
      #   raise ValueError('Cannot decrypt message')
      # # without digest
      ciphertext = base64.b64decode(ciphertext)
      sentinel = Random.new().read(32)
      message = self.private_key.decrypt(ciphertext, sentinel)
      if sentinel == message:
        raise ValueError('Cannot decrypt message')
      return message
    return self.private_key.decrypt(base64.b64decode(ciphertext))

  def encrypt(self, plaintext: str) -> str:
    return self.encrypt_bytes(bytes(plaintext, encoding='utf-8')).decode('utf-8')

  def encrypt_bytes(self, plaintext: bytes) -> bytes:
    if self.padding == PKCS1_v1_5:
      # # with digest
      # hash = SHA1.new(plaintext)
      # return base64.b64encode(self.public_key.encrypt(plaintext + hash.digest()))
      # # without digest
      return base64.b64encode(self.public_key.encrypt(plaintext))
    return base64.b64encode(self.public_key.encrypt(plaintext))
