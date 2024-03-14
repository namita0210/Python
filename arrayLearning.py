from array import *

# vals = array('i' , [5,9,8,4,2])

# print(vals)

# print(vals.buffer_info())

# newArr = array(vals.typecode , (a*a for a in vals))
# print(newArr)

#Take input in the array from user
arr = array('i', [])
n = int(input("Enter the length of an array: "))
for  i in range (n):
    x = int(input("enter the value at pos: "))
    arr.append(x)
print(arr)    