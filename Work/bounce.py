# bounce.py
#
# Exercise 1.5

height = 100
delta = 3/5
count = 10

current = 0
while current < count:
    height = round(height * delta, 4)
    current = current + 1
    print(current, height)

