# https://dabeaz-course.github.io/practical-python/Notes/01_Introduction/06_Files.html

import os

print(os.getcwd())

# f=open('Work/Data/portfolio.csv', 'rt')
# data = f.read()


# with open('Work/Data/portfolio.csv', 'rt') as f:
#     data = f.read()

f1 = open('Work/Data/portfolio2.csv','rt')

data0 = f1.readline()
data00 = f1.readlines(3)
data1 = f1.read()
data2 = f1.read() # it will be empty

f1.close()

print(data0)
print()
print(data00)
print()
print(data1)
print()
print(data2)