# lists
# https://dabeaz-course.github.io/practical-python/Notes/01_Introduction/05_Lists.html

stringList = ['123','323', 'aaa']

numList = [1, 2, 3, '1']
print(stringList)
print(numList)

string = '1,2,3,4'
print(len(string))
arr = string.split(',')
print(arr)

string = string *3 
print(string)

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

# arr = arr2 - numList # Exception
# print(arr)

print(len(arr2))

print(arr2 * 2)

for lt in arr2:
    print(lt, end=' - ')

print()

for lt in arr2:
    print(arr2.index(lt), lt, sep=' => ', end=' - ')

print()

arr2.remove(30)
print(arr2)

arr2.remove('1') # will remove only first match
print(arr2)

# arr2.sort()     # it is not possible to sort data in int and string formats
arr2.remove('1')
arr2.sort()
print(arr2)

arr3 = arr2[2: -2] #3 - 15
print('3 - 15', arr3)

print(3 in arr3)
print(3 not in arr3)

arr4 = ['qq', 'ww', 'ee']
print('~'.join(arr4)) # work with strings array only

arr2d = [1,2,3,[4,5,6]]
print(arr2d)

print('6 =', arr2d[3][2])
