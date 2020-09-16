import base64
from M2Crypto import X509, RSA
from Crypto.Util.asn1 import DerSequence
from Crypto.PublicKey import RSA as CryptoRSA
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5
from binascii import a2b_base64

from democrypt.rsa import RsaCrypt

class X509Crypt(RsaCrypt):

  def __init__(self, private: str, public: str, padding=PKCS1_v1_5):
    lines = public.replace(" ", '').split()
    der = a2b_base64(''.join(lines[1:-1]))
    cert = DerSequence()
    cert.decode(der)
    tbs_certificate = DerSequence()
    tbs_certificate.decode(cert[0])
    subject_public_key_info = tbs_certificate[6]
    super().__init__(private, subject_public_key_info, padding)

  # def __init__(self, private: str, public: str, padding=PKCS1_v1_5):
  #   self.padding = padding
  #   self.private_key = RSA.load_key_string(bytes(private, 'utf-8'))
  #   self.public_key = X509.load_cert_string(bytes(public, 'utf-8'))

  # def decrypt_bytes(self, ciphertext: bytes) -> bytes:
  #   return self.private_key.private_decrypt(base64.b64decode(ciphertext), RSA.pkcs1_oaep_padding)

  # def encrypt_bytes(self, plaintext: bytes) -> bytes:
  #   return base64.b64encode(self.public_key.get_pubkey().get_rsa().public_encrypt(plaintext, RSA.pkcs1_oaep_padding))
