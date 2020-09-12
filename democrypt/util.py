import random

def rand_string(size: int = 16) -> str:
  return ''.join([chr(random.randint(0, 0xFF)) for i in range(size)])

data = [
  'th1s1smyp@ssw0rd',
  rand_string(4),
  rand_string(16),
  rand_string(100)
]
aes128Hash = '1234567890123456'
aes192Hash = '123456789012345612345678'
aes256Hash = '12345678901234561234567890123456'
