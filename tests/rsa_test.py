"""Testing democrypt.Rsa"""

###
# Model for using UnitTest
###

import unittest
from pathlib import Path
from democrypt.rsa import RsaCrypt
from democrypt.util import data, CS_RSA_PKCS1V1_5, GO_RSA_PKCS1V1_5, JS_RSA_PKCS1V1_5, CS_RSA_OAEP, GO_RSA_OAEP, JS_RSA_OAEP
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5

class RsaTestCase(unittest.TestCase):
  """`hello` Test Case"""

  def setUp(self):
    with open(Path(__file__).parent / '../cert/rsa/cert.pem') as pub:
      with open(Path(__file__).parent / '../cert/rsa/key.pem') as priv:
        self.rsa_pkcs1v15 = RsaCrypt(priv.read(), pub.read())
        priv.close()
        pub.close()
    with open(Path(__file__).parent / '../cert/rsa/cert.pem') as pub:
      with open(Path(__file__).parent / '../cert/rsa/key.pem') as priv:
        self.rsa_oaep = RsaCrypt(priv.read(), pub.read(), padding=PKCS1_OAEP)
        priv.close()
        pub.close()

  def test_new(self):
    """Testing instance"""
    self.assertIsInstance(self.rsa_pkcs1v15, RsaCrypt)

  def test_encrypt_decrypt(self):
    """Test encrypt & decrypt"""
    for item in data:
      encrypted = self.rsa_pkcs1v15.encrypt(plaintext=item)
      self.assertEqual(type(encrypted), str)

      decrypted = self.rsa_pkcs1v15.decrypt(ciphertext=encrypted)
      self.assertEqual(decrypted, item)

  def test_encrypt_decrypt_oaep(self):
    """Test encrypt & decrypt"""
    for item in data:
      encrypted = self.rsa_oaep.encrypt(plaintext=item)
      self.assertEqual(type(encrypted), str)

      decrypted = self.rsa_oaep.decrypt(ciphertext=encrypted)
      self.assertEqual(decrypted, item)

  def test_decrypt_from_csharp_pkcs1v15(self):
    """Test decrypt from C#"""
    decrypted = self.rsa_pkcs1v15.decrypt(CS_RSA_PKCS1V1_5)
    self.assertEqual(decrypted, data[0])

  def test_decrypt_from_csharp_oaep(self):
    """Test decrypt from C#"""
    decrypted = self.rsa_oaep.decrypt(CS_RSA_OAEP)
    self.assertEqual(decrypted, data[0])

  def test_decrypt_from_go_pkcs1v15(self):
    """Test decrypt from Go"""
    decrypted = self.rsa_pkcs1v15.decrypt(GO_RSA_PKCS1V1_5)
    self.assertEqual(decrypted, data[0])

  @unittest.skip("go oaep is not working ?")
  def test_decrypt_from_go_oaep(self):
    """Test decrypt from Go"""
    decrypted = self.rsa_oaep.decrypt(GO_RSA_OAEP)
    self.assertEqual(decrypted, data[0])

  def test_decrypt_from_js_pkcs1v15(self):
    """Test decrypt from C#"""
    decrypted = self.rsa_pkcs1v15.decrypt(JS_RSA_PKCS1V1_5)
    self.assertEqual(decrypted, data[0])

  def test_decrypt_from_js_oaep(self):
    """Test decrypt from C#"""
    decrypted = self.rsa_oaep.decrypt(JS_RSA_OAEP)
    self.assertEqual(decrypted, data[0])
