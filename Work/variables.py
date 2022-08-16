# variables tests
from operator import truediv


a = 1
b = True # True == 1
# c = true
d = 1.23
f = 2 + 4j #complex

print(a, a+b, a+d, a+f)

a = 0o123
b = -12372834817409874309817491347091825710098457189034790184738570109847511098357918345798324573924858923789528345792843594238579340287
c = 0b1010101
d = 0x828742983423f23090a0290348230948209bb0980c908098d098098098990890e908098098f4242342

print(a, b, c, d)

a = 11
b = 3
print('a=', a, ' b=', b)
print('a/b', a/b)
print('a//b', a//b) # integer part
print('a%b', a%b)
print('a**b', a**b) #power

a = 2.1 + 4.2 # = 6.300000000000001

if a == 6.3:
    print('True - ', a)
else:
    print('False - ', a)

a= a+.4

print('a=', a, ' int(a)=', int(a))
print('b=', b, ' float(b)=', float(b))


s = '123.744'
print(type(s), s)
s = float(s)
print(type(s), s)

s = '123'
print(type(s), s)
s = int(s)          # int and float from str will validate the format int('123.456') is incorrect
print(type(s), s)

print(bool("False"))    #True

print(bool(""))         #False
print(bool(int("0")))   #False


# Single quote
a = 'Yeah but no but yeah but...'

# Double quote
b = "computer says no"

# Triple quotes
c = '''
Look into my eyes, look into my eyes, the eyes, the eyes, the eyes,
not around the eyes,
don't look around the eyes,
look into my eyes, you're under.
'''

print(a, b, c)

print('\"Hi\" \nQQQ\r1\t2\'\\\' \u27F0  \u27FF  \u27F3')


a = 'Hello world'
print('a=', a, ' len(a) = ', len(a))
print('H - ',a[0], ' l - ', a[-2])
print('He - ',a[:2], ' ld - ', a[-2:])
print('ell - ',a[1:4], ' orl - ', a[-4:-1], ' orl - ', a[7:-1], ' orl - ', a[7:10], ' orl - ', a[7:len(a)-1])
print('orld -', a[-4:0], 'orld - ', a[7:0], 'H - ', a[0:0], 'H - ', a[:0])

#   H   e   l   l   o       w   o   r   l   d   
#   0   1   2   3   4   5   6   7   8   9   10  <-index forward
#   -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1  <-index backward
#   [:2] - (2) is NOT included
#   [-2:] - [-2] is included
#   [0:4] - [0] - included (4) - NOT included
#   [-4:-1] - [-4] - include (-1) - exclude
#   [7:-1] - [7] - left include (-1) - right exclude
#   [7:10] - [7] - left include (10) - right exclude
#   [7:len(a)-1] - [7] - left include (len(a)-1) - right exclude
#   if right=0 - [-4:0], [7:0], [0:0], [:0] - a couple of spaces
#       !!! So, general rule "left included - right excluded, right!=0" !!!

symbols = 'AAPL,IBM,MSFT,YHOO,SCO'
print(symbols)
symbols = symbols + ',GOOG'
print(symbols)
symbols = 'HPQ,' + symbols
print(symbols)
symbols = (symbols + ',') * 3
print(symbols)

print('GOOG' in symbols)
print('GO-OG' not in symbols)

print(symbols.lower())
print(symbols.upper())

a = b'Hello'
print(a[1])

# For more information about the re module, see the official documentation at https://docs.python.org/library/re.html.
# dir() produces a list of all operations that can appear after the (.). 
# Use the help() command to get more information about a specific operation:
