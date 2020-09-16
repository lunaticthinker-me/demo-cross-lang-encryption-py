from Crypto.Cipher import AES
from democrypt.aes import AesCrypt
from democrypt.rsa import RsaCrypt
from democrypt.x509 import X509Crypt
from democrypt.util import aes128Hash, aes192Hash, aes256Hash, data
from pathlib import Path
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5

print('// AES Encrypted Values:')
print("PY_AES_CFB8_128 = '{}'".format(AesCrypt(aes128Hash).encrypt(data[0])))
print("PY_AES_CFB8_192 = '{}'".format(AesCrypt(aes192Hash).encrypt(data[0])))
print("PY_AES_CFB8_256 = '{}'".format(AesCrypt(aes256Hash).encrypt(data[0])))
print("PY_AES_CBC_128 = '{}'".format(AesCrypt(aes128Hash, AES.MODE_CBC).encrypt(data[0])))
print("PY_AES_CBC_192 = '{}'".format(AesCrypt(aes192Hash, AES.MODE_CBC).encrypt(data[0])))
print("PY_AES_CBC_256 = '{}'".format(AesCrypt(aes256Hash, AES.MODE_CBC).encrypt(data[0])))

print('// RSA Encrypted Values:')
with open(Path(__file__).parent / 'cert/rsa/cert.pem') as pub:
  with open(Path(__file__).parent / 'cert/rsa/key.pem') as priv:
    rsa_pkcs1v15 = RsaCrypt(priv.read(), pub.read(), padding=PKCS1_v1_5)
    print("PY_RSA_PKCS1V1_5 = '{}'".format(rsa_pkcs1v15.encrypt(data[0])))
    priv.close()
    pub.close()
with open(Path(__file__).parent / 'cert/rsa/cert.pem') as pub:
  with open(Path(__file__).parent / 'cert/rsa/key.pem') as priv:
    rsa_oaep = RsaCrypt(priv.read(), pub.read(), padding=PKCS1_OAEP)
    print("PY_RSA_OAEP = '{}'".format(rsa_oaep.encrypt(data[0])))
    priv.close()
    pub.close()

print('// X509 Encrypted Values:')
with open(Path(__file__).parent / 'cert/x509/cert.pem') as pub:
  with open(Path(__file__).parent / 'cert/x509/key.pem') as priv:
    x509 = X509Crypt(priv.read(), pub.read(), padding=PKCS1_v1_5)
    print("PY_X509_PKCS1V1_5 = '{}'".format(x509.encrypt(data[0])))
with open(Path(__file__).parent / 'cert/x509/cert.pem') as pub:
  with open(Path(__file__).parent / 'cert/x509/key.pem') as priv:
    x509 = X509Crypt(priv.read(), pub.read(), padding=PKCS1_OAEP)
    print("PY_X509_OAEP = '{}'".format(x509.encrypt(data[0])))
