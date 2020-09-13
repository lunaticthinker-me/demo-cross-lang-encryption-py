"""Testing democrypt.X509"""

###
# Model for using UnitTest
###

import unittest
from pathlib import Path
from democrypt.x509 import X509Crypt
from democrypt.util import data, JS_RSA, GO_RSA

class X509TestCase(unittest.TestCase):
  """`hello` Test Case"""

  def setUp(self):
    with open(Path(__file__).parent / '../cert/x509/cert.pem') as pub:
      with open(Path(__file__).parent / '../cert/x509/key.pem') as priv:
        self.x509 = X509Crypt(priv.read(), pub.read())
        priv.close()
        pub.close()

  def test_new(self):
    """Testing instance"""
    self.assertIsInstance(self.x509, X509Crypt)

  def test_encrypt_decrypt(self):
    """Test encrypt & decrypt"""
    for item in data:
      encrypted = self.x509.encrypt(plaintext=item)
      self.assertEqual(type(encrypted), str)

      decrypted = self.x509.decrypt(ciphertext=encrypted)
      self.assertEqual(decrypted, item)

  # def test_decrypt_from_csharp(self):
  #   """Test decrypt from C#"""
  #   decrypted = self.x509.decrypt(JS_RSA)
  #   self.assertEqual(decrypted, data[0])
  #
  # def test_decrypt_from_js(self):
  #   """Test decrypt from JS"""
  #   decrypted = self.x509.decrypt(JS_RSA)
  #   self.assertEqual(decrypted, data[0])
  #
  # def test_decrypt_from_go(self):
  #   """Test decrypt from Go"""
  #   decrypted = self.x509.decrypt(GO_RSA)
  #   self.assertEqual(decrypted, data[0])
