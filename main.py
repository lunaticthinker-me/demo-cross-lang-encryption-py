from Crypto.Cipher import AES
from democrypt.aes import AesCrypt
from democrypt.rsa import RsaCrypt
from democrypt.x509 import X509Crypt
from democrypt.util import aes128Hash, aes192Hash, aes256Hash, data
from pathlib import Path
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5


for prefix in [("C#", "public static string PY", '"'), ("Go", "var PY", '"'), ("Js", "export const PY", "'")]:
  (lang, prefix, quote) = prefix

  print("// {}".format(lang))
  print("")
  print('// AES Encrypted Values:')
  print("{prefix}_AES_CFB8_128 = {quote}{crypto}{quote}".format(crypto=AesCrypt(aes128Hash).encrypt(data[0]), prefix=prefix, quote=quote))
  print("{prefix}_AES_CFB8_192 = {quote}{crypto}{quote}".format(crypto=AesCrypt(aes192Hash).encrypt(data[0]), prefix=prefix, quote=quote))
  print("{prefix}_AES_CFB8_256 = {quote}{crypto}{quote}".format(crypto=AesCrypt(aes256Hash).encrypt(data[0]), prefix=prefix, quote=quote))
  print("{prefix}_AES_CBC_128 = {quote}{crypto}{quote}".format(crypto=AesCrypt(aes128Hash, AES.MODE_CBC).encrypt(data[0]), prefix=prefix, quote=quote))
  print("{prefix}_AES_CBC_192 = {quote}{crypto}{quote}".format(crypto=AesCrypt(aes192Hash, AES.MODE_CBC).encrypt(data[0]), prefix=prefix, quote=quote))
  print("{prefix}_AES_CBC_256 = {quote}{crypto}{quote}".format(crypto=AesCrypt(aes256Hash, AES.MODE_CBC).encrypt(data[0]), prefix=prefix, quote=quote))
  print("")
  print('// RSA Encrypted Values:')
  with open(Path(__file__).parent / 'cert/rsa/cert.pem') as pub:
    with open(Path(__file__).parent / 'cert/rsa/key.pem') as priv:
      rsa_pkcs1v15 = RsaCrypt(priv.read(), pub.read(), padding=PKCS1_v1_5)
      print("{prefix}_RSA_PKCS1V1_5 = {quote}{crypto}{quote}".format(crypto=rsa_pkcs1v15.encrypt(data[0]), prefix=prefix, quote=quote))
      priv.close()
      pub.close()
  with open(Path(__file__).parent / 'cert/rsa/cert.pem') as pub:
    with open(Path(__file__).parent / 'cert/rsa/key.pem') as priv:
      rsa_oaep = RsaCrypt(priv.read(), pub.read(), padding=PKCS1_OAEP)
      print("{prefix}_RSA_OAEP = {quote}{crypto}{quote}".format(crypto=rsa_oaep.encrypt(data[0]), prefix=prefix, quote=quote))
      priv.close()
      pub.close()
  print("")
  print('// X509 Encrypted Values:')
  with open(Path(__file__).parent / 'cert/x509/cert.pem') as pub:
    with open(Path(__file__).parent / 'cert/x509/key.pem') as priv:
      x509 = X509Crypt(priv.read(), pub.read(), padding=PKCS1_v1_5)
      print("{prefix}_X509_PKCS1V1_5 = {quote}{crypto}{quote}".format(crypto=x509.encrypt(data[0]), prefix=prefix, quote=quote))
  with open(Path(__file__).parent / 'cert/x509/cert.pem') as pub:
    with open(Path(__file__).parent / 'cert/x509/key.pem') as priv:
      x509 = X509Crypt(priv.read(), pub.read(), padding=PKCS1_OAEP)
      print("{prefix}_X509_OAEP = {quote}{crypto}{quote}".format(crypto=x509.encrypt(data[0]), prefix=prefix, quote=quote))
  print("")
  print("")
