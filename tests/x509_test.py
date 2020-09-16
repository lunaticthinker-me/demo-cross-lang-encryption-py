"""Testing democrypt.X509"""

###
# Model for using UnitTest
###

import unittest
from pathlib import Path
from democrypt.x509 import X509Crypt
from democrypt.util import data, CS_X509_PKCS1V1_5, GO_X509_PKCS1V1_5, JS_X509_PKCS1V1_5, CS_X509_OAEP, GO_X509_OAEP, JS_X509_OAEP
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5

class X509TestCase(unittest.TestCase):
  """`hello` Testing Case"""

  def setUp(self):
    with open(Path(__file__).parent / '../cert/x509/cert.pem') as pub:
      with open(Path(__file__).parent / '../cert/x509/key.pem') as priv:
        self.x509_pkcs1v15 = X509Crypt(priv.read(), pub.read())
        priv.close()
        pub.close()
    with open(Path(__file__).parent / '../cert/x509/cert.pem') as pub:
      with open(Path(__file__).parent / '../cert/x509/key.pem') as priv:
        self.x509_oaep = X509Crypt(priv.read(), pub.read(), padding=PKCS1_OAEP)
        priv.close()
        pub.close()

  def test_new(self):
    """Testing instance"""
    self.assertIsInstance(self.x509_oaep, X509Crypt)

  def test_encrypt_decrypt_pkcs1v15(self):
    """Testing encrypt & decrypt"""
    for item in data:
      encrypted = self.x509_pkcs1v15.encrypt(plaintext=item)
      self.assertEqual(type(encrypted), str)

      decrypted = self.x509_pkcs1v15.decrypt(ciphertext=encrypted)
      self.assertEqual(decrypted, item)

  def test_encrypt_decrypt_oaep(self):
    """Testing encrypt & decrypt"""
    for item in data:
      encrypted = self.x509_oaep.encrypt(plaintext=item)
      self.assertEqual(type(encrypted), str)

      decrypted = self.x509_oaep.decrypt(ciphertext=encrypted)
      self.assertEqual(decrypted, item)

  # def test_decrypt_from_csharp_pkcs1v15(self):
  #   """Testing X509 decrypt from C#"""
  #   decrypted = self.x509_pkcs1v15.decrypt(CS_X509_PKCS1V1_5)
  #   self.assertEqual(decrypted, data[0])
  #
  # def test_decrypt_from_csharp_oaep(self):
  #   """Testing X509 decrypt from C#"""
  #   decrypted = self.x509_oaep.decrypt(CS_X509_OAEP)
  #   self.assertEqual(decrypted, data[0])

  def test_decrypt_from_go_pkcs1v15(self):
    """Testing X509 decrypt from Go"""
    decrypted = self.x509_pkcs1v15.decrypt(GO_X509_PKCS1V1_5)
    self.assertEqual(decrypted, data[0])

  @unittest.skip("go oaep is not working ?")
  def test_decrypt_from_go_oaep(self):
    """Testing X509 decrypt from Go"""
    decrypted = self.x509_oaep.decrypt(GO_X509_OAEP)
    self.assertEqual(decrypted, data[0])

  def test_decrypt_from_js_pkcs1v15(self):
    """Testing X509/PKCS1V1_5 decrypt from Js"""
    decrypted = self.x509_pkcs1v15.decrypt(JS_X509_PKCS1V1_5)
    self.assertEqual(decrypted, data[0])

  @unittest.skip("python doesn't like JS OAEP padding")
  def test_decrypt_from_js_oaep(self):
    """Testing X509/OAEP decrypt from Js"""
    decrypted = self.x509_oaep.decrypt(JS_X509_OAEP)
    self.assertEqual(decrypted, data[0])
