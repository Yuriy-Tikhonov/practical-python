# lists
# https://dabeaz-course.github.io/practical-python/Notes/01_Introduction/05_Lists.html

stringList = ['123','323', 'aaa']
numList = [1, 2, 3, '1']
print(stringList)
print(numList)

string = '1,2,3,4'
arr = string.split(',')
print(arr)

str = '1, 2, 3'
arr = str.split(', ')
print(arr)

a,b,c=arr
print(a,b,c)

a,b,c = 3,2,1
print(a,b,c)

arr.append(4)
arr[2]=30
arr[-3]=20
print(arr)

arr.insert(1,15) # index from 0, insert BEFORE index 1
print(arr)

arr.insert(-2,25) # index from -1, insert BEFORE index -2
print(arr)

arr2 = arr + numList
print(arr2)

