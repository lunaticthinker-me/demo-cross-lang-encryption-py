"""Testing democrypt.aes"""

###
# Model for using UnitTest
###

import unittest
from Crypto.Cipher import AES
from democrypt.aes import AesCrypt
from democrypt.util import data, aes128Hash, aes192Hash, aes256Hash, \
  CS_AES_CFB8_128, CS_AES_CFB8_192, CS_AES_CFB8_256, CS_AES_CBC_128, CS_AES_CBC_192, CS_AES_CBC_256, \
  JS_AES_CFB8_128, JS_AES_CFB8_192, JS_AES_CFB8_256, JS_AES_CBC_128, JS_AES_CBC_192, JS_AES_CBC_256, \
  GO_AES_CFB_128, GO_AES_CFB_192, GO_AES_CFB_256, GO_AES_CBC_128, GO_AES_CBC_192, GO_AES_CBC_256


class AesTestCase(unittest.TestCase):
  """`AesCrypt` Test Case"""

  def setUp(self):
    self.aes128Cfb = AesCrypt(aes128Hash)
    self.aes192Cfb = AesCrypt(aes192Hash)
    self.aes256Cfb = AesCrypt(aes256Hash)
    self.aes128Cbc = AesCrypt(aes128Hash, AES.MODE_CBC)
    self.aes192Cbc = AesCrypt(aes192Hash, AES.MODE_CBC)
    self.aes256Cbc = AesCrypt(aes256Hash, AES.MODE_CBC)

  def test_new(self):
    """Testing instance"""
    self.assertIsInstance(self.aes128Cfb, AesCrypt)

  def test_pkcs7_padding(self):
    """Testing PKCS7 padding"""
    for item in data:
      bitem = bytes(item, 'utf-8')
      padded = self.aes128Cfb.pkcs7_padding(bitem)
      self.assertEqual(type(padded), bytes)

      trimed = self.aes128Cfb.pkcs7_trimming(padded)
      self.assertEqual(len(trimed), len(bitem))
      self.assertEqual(trimed, bitem)

  def test_encrypt_decrypt_128_cfb(self):
    """Testing encrypt/decrypt 128 bytes hash, CFB mode"""
    for item in data:
      encrypted = self.aes128Cfb.encrypt(plaintext=item)
      self.assertEqual(type(encrypted), str)

      decrypted = self.aes128Cfb.decrypt(ciphertext=encrypted)
      self.assertEqual(decrypted, item)

  def test_encrypt_decrypt_192_cfb(self):
    """Testing encrypt/decrypt 192 bytes hash, CFB mode"""
    aes = AesCrypt(aes192Hash)
    for item in data:
      encrypted = self.aes192Cfb.encrypt(plaintext=item)
      self.assertEqual(type(encrypted), str)

      decrypted = self.aes192Cfb.decrypt(ciphertext=encrypted)
      self.assertEqual(decrypted, item)

  def test_encrypt_decrypt_256_cfb(self):
    """Testing encrypt/decrypt 256 bytes hash, CFB mode"""
    for item in data:
      encrypted = self.aes256Cfb.encrypt(plaintext=item)
      self.assertEqual(type(encrypted), str)

      decrypted = self.aes256Cfb.decrypt(ciphertext=encrypted)
      self.assertEqual(decrypted, item)

  def test_encrypt_decrypt_128_cbc(self):
    """Testing encrypt/decrypt 128 bytes hash, CBC mode"""
    for item in data:
      encrypted = self.aes128Cbc.encrypt(plaintext=item)
      self.assertEqual(type(encrypted), str)

      decrypted = self.aes128Cbc.decrypt(ciphertext=encrypted)
      self.assertEqual(decrypted, item)

  def test_encrypt_decrypt_192_cbc(self):
    """Testing encrypt/decrypt 192 bytes hash, CBC mode"""
    for item in data:
      encrypted = self.aes192Cbc.encrypt(plaintext=item)
      self.assertEqual(type(encrypted), str)

      decrypted = self.aes192Cbc.decrypt(ciphertext=encrypted)
      self.assertEqual(decrypted, item)

  def test_encrypt_decrypt_256_cbc(self):
    """Testing encrypt/decrypt 256 bytes hash, CBC mode"""
    for item in data:
      encrypted = self.aes256Cbc.encrypt(plaintext=item)
      self.assertEqual(type(encrypted), str)

      decrypted = self.aes256Cbc.decrypt(ciphertext=encrypted)
      self.assertEqual(decrypted, item)

  def test_decrypt_from_cs_128_cfb(self):
    """Testing decrypt from CS AES 128 bytes hash, CFB mode"""
    decrypted = self.aes128Cfb.decrypt(CS_AES_CFB8_128)
    self.assertEqual(decrypted, data[0])

  def test_decrypt_from_cs_192_cfb(self):
    """Testing decrypt from CS AES 128 bytes hash, CFB mode"""
    decrypted = self.aes192Cfb.decrypt(CS_AES_CFB8_192)
    self.assertEqual(decrypted, data[0])

  def test_decrypt_from_cs_256_cfb(self):
    """Testing decrypt from CS AES 256 bytes hash, CFB mode"""
    decrypted = self.aes256Cfb.decrypt(CS_AES_CFB8_256)
    self.assertEqual(decrypted, data[0])

  def test_decrypt_from_cs_128_cbc(self):
    """Testing decrypt from CS AES 128 bytes hash, CBC mode"""
    decrypted = self.aes128Cbc.decrypt(CS_AES_CBC_128)
    self.assertEqual(decrypted, data[0])

  def test_decrypt_from_cs_192_cbc(self):
    """Testing decrypt from CS AES 128 bytes hash, CBC mode"""
    decrypted = self.aes192Cbc.decrypt(CS_AES_CBC_192)
    self.assertEqual(decrypted, data[0])

  def test_decrypt_from_cs_256_cbc(self):
    """Testing decrypt from CS AES 256 bytes hash, CBC mode"""
    decrypted = self.aes256Cbc.decrypt(CS_AES_CBC_256)
    self.assertEqual(decrypted, data[0])

  # def test_decrypt_from_go_128_cfb(self):
  #   """Testing decrypt from GO AES 128 bytes hash, CFB mode"""
  #   decrypted = self.aes128Cfb.decrypt(GO_AES_CFB_128)
  #   self.assertEqual(decrypted, data[0])
  #
  # def test_decrypt_from_go_192_cfb(self):
  #   """Testing decrypt from GO AES 128 bytes hash, CFB mode"""
  #   decrypted = self.aes192Cfb.decrypt(GO_AES_CFB_192)
  #   self.assertEqual(decrypted, data[0])
  #
  # def test_decrypt_from_go_256_cfb(self):
  #   """Testing decrypt from GO AES 256 bytes hash, CFB mode"""
  #   decrypted = self.aes256Cfb.decrypt(GO_AES_CFB_256)
  #   self.assertEqual(decrypted, data[0])

  def test_decrypt_from_go_128_cbc(self):
    """Testing decrypt from GO AES 128 bytes hash, CBC mode"""
    decrypted = self.aes128Cbc.decrypt(GO_AES_CBC_128)
    self.assertEqual(decrypted, data[0])

  def test_decrypt_from_go_192_cbc(self):
    """Testing decrypt from GO AES 128 bytes hash, CBC mode"""
    decrypted = self.aes192Cbc.decrypt(GO_AES_CBC_192)
    self.assertEqual(decrypted, data[0])

  def test_decrypt_from_go_256_cbc(self):
    """Testing decrypt from GO AES 256 bytes hash, CBC mode"""
    decrypted = self.aes256Cbc.decrypt(GO_AES_CBC_256)
    self.assertEqual(decrypted, data[0])

  def test_decrypt_from_js_128_cfb(self):
    """Testing decrypt from JS AES 128 bytes hash, CFB mode"""
    decrypted = self.aes128Cfb.decrypt(JS_AES_CFB8_128)
    self.assertEqual(decrypted, data[0])

  def test_decrypt_from_js_192_cfb(self):
    """Testing decrypt from JS AES 128 bytes hash, CFB mode"""
    decrypted = self.aes192Cfb.decrypt(JS_AES_CFB8_192)
    self.assertEqual(decrypted, data[0])

  def test_decrypt_from_js_256_cfb(self):
    """Testing decrypt from JS AES 256 bytes hash, CFB mode"""
    decrypted = self.aes256Cfb.decrypt(JS_AES_CFB8_256)
    self.assertEqual(decrypted, data[0])

  def test_decrypt_from_js_128_cbc(self):
    """Testing decrypt from JS AES 128 bytes hash, CBC mode"""
    decrypted = self.aes128Cbc.decrypt(JS_AES_CBC_128)
    self.assertEqual(decrypted, data[0])

  def test_decrypt_from_js_192_cbc(self):
    """Testing decrypt from JS AES 128 bytes hash, CBC mode"""
    decrypted = self.aes192Cbc.decrypt(JS_AES_CBC_192)
    self.assertEqual(decrypted, data[0])

  def test_decrypt_from_js_256_cbc(self):
    """Testing decrypt from JS AES 256 bytes hash, CBC mode"""
    decrypted = self.aes256Cbc.decrypt(JS_AES_CBC_256)
    self.assertEqual(decrypted, data[0])
