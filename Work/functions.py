# functions

def sum(a, b):
    return a+b

a = sum(1,2)
print(a)

import math
from signal import raise_signal

print(math.cos(30))

print(math.sqrt(2))

import urllib.request

urlData = urllib.request.urlopen('https://google.com')
a = urlData.read()
print(a)

try:
    int('N/A')
    int('123')
except (ValueError, RuntimeError) as exc: # several types
    print('It was Value Error')
    print(exc)
#    raise RuntimeError('Help')  # raise without processing
else:                           # no error processing block
    print('No error')
finally:
    print('finally')


# try:
#     raise RuntimeError22('Help')  # raise without processing
# except RuntimeError22 as exc: # several types
#     print('It was RuntimeError22 Error')
#     print(exc)
# else:                           # no error processing block
#     print('No error')
# finally:
#     print('finally')
