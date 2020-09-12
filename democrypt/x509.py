import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

class X509Crypt:

  def __init__(self, private: str, public: str):
    self.public = serialization.load_pem_public_key(
        public,
        backend=default_backend()
    )
    self.private = serialization.load_pem_private_key(
        private,
        password=None,
        backend=default_backend()
    )

  def decrypt(self, ciphertext: str) -> str:
    decoded = base64.b64decode(bytes(ciphertext, 'utf-8'))
    return self.private.decrypt(
      decoded,
      padding.OAEP(
          mgf=padding.MGF1(algorithm=hashes.SHA256()),
          algorithm=hashes.SHA256(),
          label=None
      )
   )

  def encrypt(self, plaintext: str) -> str:
    cipher = self.public.encrypt(
      plaintext,
      padding.OAEP(
          mgf=padding.MGF1(algorithm=hashes.SHA256()),
          algorithm=hashes.SHA256(),
          label=None
      )
    )
    return base64.b16encode(cipher).decode('utf-8')
