import base64
from M2Crypto import SMIME, X509, RSA

class X509Crypt:

  def __init__(self, private: str, public: str):
    self.mime = SMIME.SMIME()
    self.private_key = RSA.load_key_string(bytes(private, 'utf-8'))
    self.public_key = X509.load_cert_string(bytes(public, 'utf-8'))

  def decrypt(self, ciphertext: str) -> str:
    return self.decrypt_bytes(bytes(ciphertext, 'utf-8')).decode('utf-8')

  def decrypt_bytes(self, ciphertext: bytes) -> bytes:
    return self.private_key.private_decrypt(base64.b64decode(ciphertext), RSA.pkcs1_padding)

  def encrypt(self, plaintext: str) -> str:
    return self.encrypt_bytes(bytes(plaintext, 'utf-8')).decode('utf-8')

  def encrypt_bytes(self, plaintext: bytes) -> bytes:
    return base64.b64encode(self.public_key.get_pubkey().get_rsa().public_encrypt(plaintext, RSA.pkcs1_padding))
