from Crypto.Cipher import AES
from democrypt.aes import AesCrypt
from democrypt.util import aes128Hash, aes192Hash, aes256Hash, data

print('AES Encrypted Values:')
print('CFB8 128 => {}'.format(AesCrypt(aes128Hash).encrypt(data[0])))
print('CFB8 192 => {}'.format(AesCrypt(aes192Hash).encrypt(data[0])))
print('CFB8 256 => {}'.format(AesCrypt(aes256Hash).encrypt(data[0])))
print('CBC 128 => {}'.format(AesCrypt(aes128Hash, AES.MODE_CBC).encrypt(data[0])))
print('CBC 192 => {}'.format(AesCrypt(aes192Hash, AES.MODE_CBC).encrypt(data[0])))
print('CBC 256 => {}'.format(AesCrypt(aes256Hash, AES.MODE_CBC).encrypt(data[0])))

# RSA Encrypted Values:
# ejxZ8nhP78EcPV9htkveKjSYpML6WYfwCo+GXQEzeXnvNSEYDY78nr3qZ5lTqNrMMUlcdNIVOygFzRHMERs/UloZdnN/9ZviS40tEaLzZArsbEU9CE1avtAbAs2Fm1uQSbgX0tyHbhF/1nwOPc5VOlpeiGv/44T1yuKuK7H4C8/RhpLDFjs3BhQIML7D/xIxyDW0AQCuktCDX91R6UPSbhW2IFDnEZRWnxRkjhXo/RG2md40iIIaS7CYio1/6wYkuLoU1fHY3ZObjX4CPOINra38kYueX9KDg+dBOIJPeqAJwEdcrRFWOgo4Zk40gufXYWLPHXgeMVvGGBdAYfhCtQ==
#
# X509 Encrypted Values:
# hZwqcWtyUqud8icPjRPtq3SzjYUnY9Tyfqq5yCQtYD
