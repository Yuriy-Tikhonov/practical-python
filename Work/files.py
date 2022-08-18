# https://dabeaz-course.github.io/practical-python/Notes/01_Introduction/06_Files.html

import os

print(os.getcwd())

f1 = open('Work/Data/portfolio.csv','rt')

data0 = f1.readline()
data00 = f1.readlines(20) # 20 - the parameter is in bytes 
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

print('-------------------')

with open('Work/Data/portfolio.csv', 'rt') as f:
    data_with = f.read()
    print(data_with)
    print()

print('-------------------')
with open('Work/Data/portfolio.csv', 'rt') as f:
    for line in f:
        print(line)
        # print('-=-=-=-=-=')

print('-------------------')
with open('Work/Data/portfolio.csv', 'rt') as fi:
    with open('Work/Data/output', 'wt') as fw:
        for line in fi:
            fw.write(line)
            print('-=-=-=-=-=-=-=-=-=', file=fw)

import gzip

with gzip.open('Work/Data/portfolio.csv.gz', 'rt') as gf:
    for line in gf:
        print(line)

