# Null is called None
import math

# Variables can change type
n = None
n = 4

print(n)

# If condition
a = 1

if a > 2:
    a -= 1
elif a < 0:
    a += 2
else:
    a *= 10

# and = &&
# or = ||
# multiline condition needs parentheses
if (n > 2 and
        n != a):
    print("valid")

# While loop
n = 0
while n < 5:
    n += 1

# For loop from i =0 to i = 4; 5 is not included
for i in range(5):
    print(i)

# For loop from i =2 to i = 4; 5 is not included
for i in range(2, 5):
    print(i)

# descending loop
for i in range(5, 1, -1):
    print(i)

# Division is decimal by default
print(5 / 2)  # answer is: 2.5

# Division by integer is done using //
print(5 // 2)  # answer is: 2

# Negative integer division is round down
print(-3 // 2)  # answer is -2
# work around: use decimal division and covert to int
print(int(-3 / 2))  # answer is -1

print(10 % 3)  # similar with other languages
print(math.floor(3 / 2))  # round down
print(math.ceil(3 / 2))  # round up
print(math.pow(3, 2))

# Max / Min Inf
float("inf")
float("-inf")

# Arrays == List
arr = [1, 2, 3, 4]
print(arr)

# can be used as stack
arr.append(6)
print(arr)

arr.pop()
print(arr)

arr.insert(1, 7)  # this in O(n) operation
arr[0] = 8

# Sized array
n = 5
arr = [1] * n

# last index of array
print(arr[-1])

#   slice in array
arr[1:3]

# unpacking -- pattern matching
a, b, c = [1, 2, 3]

# Iterate throw array
# Using index
for i in range(len(arr)):
    print(i)

# Without index
for a in arr:
    print(a)

# With index and value
for i, n in enumerate(arr):
    print(i, n)

# Iterate throw multiple arrays
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print((n1, n2))

# reverse array
nums = [1, 2, 3]
nums.reverse()

# Sorting array
nums = [5, 6, 1, 2, 8, 3]
nums.sort()
nums.sort(reverse=True)

# Custom sort
arr = ["bob", "alice"]
arr.sort(key=lambda x: len(x))

# List Comprehension
arr = [i + i for i in range(5)]
print(arr)

# 2-D List -> gird
arr = [[0] * 4 for i in range(4)]
print(arr)

# Strings - immutable
s = "abc"
print(s[0:2])

# string to int
print(int("1234") + int("1234"))
print(str(123) + str(23123))

# ascii value of a char
print(ord("a"))

# join list of string
strings = ["ab", "cd", "ef"]
print("".join(strings))

# Queue
from collections import deque

deque = deque()
deque.append(1)
deque.append(2)

print(deque)

deque.popleft()
deque.appendleft(21)

# HashSet
mySet = set()
mySet.add(1)
mySet.add(2)

print(len(mySet))

print(2 in mySet)
# remove values
mySet.remove(2)

# Set comprehension
mySet = {i for i in range(1, 5)}

# HashMap
myHashMap = {}
myHashMap["alice"] = 88
myHashMap["bob"] = 58

myMap = {"alice": 90, "bob": 65}

# Dict comprehension
dicMyMap = {i: 2 * i for i in range(3)}
print(dicMyMap)

# loop through map
for key in myMap:
    print(key, myMap[key])

for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key, val)

# Touples
tup = (1, 2, 3)
print(tup)

myMap = {(1, 2): 3}

# Heaps
import heapq

minHeap = []
minHeap.heappush(minHeap, 3)
minHeap.heappush(minHeap, 2)

while len(minHeap):
    print(heapq.heappop(minHeap))


# Max heap can be obtained by multiply the value to -1


def double(arr, val):
    def helper():
        for i, n in enumerate(arr):
            arr[i] *= 2

            # will only modify val in the helper function

            # will modify val outside helper function
            nonlocal val
            val *= 2

    helper()
    nums = [1, 2]
    val = 3
    double(nums, val)
