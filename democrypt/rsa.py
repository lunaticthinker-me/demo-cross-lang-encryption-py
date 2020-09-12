from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5, PKCS1_OAEP
import base64

class RsaCrypt:

  def __init__(self, private: str, public: str):
    self.private = PKCS1_v1_5.new(private)
    self.public = PKCS1_OAEP.new(RSA.importKey(public))

  def decrypt(self, ciphertext: str) -> str:
    decoded = base64.b64decode(bytes(ciphertext, 'utf-8'))
    return self.private.decrypt(decoded).decode('utf-8')

  def encrypt(self, plaintext: str) -> str:
    cipher = self.public.encrypt(plaintext)
    return base64.b16encode(cipher).decode('utf-8')
