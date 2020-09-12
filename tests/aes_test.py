"""Testing democrypt.aes"""

###
# Model for using UnitTest
###

import unittest
import math
from Crypto.Cipher import AES
from democrypt.aes import AesCrypt
from democrypt.util import data, aes128Hash, aes192Hash, aes256Hash

class AesTestCase(unittest.TestCase):
  """`hello` Test Case"""

  def test_new(self):
    """Testing instance"""
    aes = AesCrypt(aes128Hash)
    self.assertIsInstance(aes, AesCrypt)

  def test_pkcs7_padding(self):
    """Testing PKCS7 padding"""
    aes = AesCrypt(aes128Hash)
    BS = AES.block_size
    for item in data:
      padded = aes.pkcs7_padding(item)
      self.assertEqual(type(padded), str)

      trimed = aes.pkcs7_trimming(padded)
      self.assertEqual(len(trimed), len(item))
      self.assertEqual(trimed, item)


  def test_encrypt_decrypt_128_cfb(self):
    """Testing encrypt/decrypt 128 bytes hash, CFB mode"""
    aes = AesCrypt(aes128Hash)
    for item in data:
      encrypted = aes.encrypt(plaintext=item)
      self.assertEqual(type(encrypted), str)

      decrypted = aes.decrypt(ciphertext=encrypted)
      self.assertEqual(decrypted, item)
