# https://dabeaz-course.github.io/practical-python/Notes/01_Introduction/06_Files.html

import os

print(os.getcwd())

f=open('Data/portfolio.csv', 'rt')
data = f.read()


with open('Data/portfolio.csv', 'rt') as f:
    data = f.read()

f1 = open('Data/portfolio2.csv','rt')

data1 = f1.read()

f1.close()

print(data1)