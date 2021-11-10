

def smallerNumbersThanCurrent(nums): 
    num_dict = {} 
    nums_sorted = sorted(nums)
    nums_2 = [] 
    for i in nums_sorted:
        num_dict[i] = nums_sorted.index(i)
    for i in nums: 
        nums_2.append(num_dict[i])
    return(nums_2)

    #return(num_sorted)


num1 = [6,5,4,8]

#print(smallerNumbersThanCurrent(num1))


def smallerNumbersThanCurrent(nums): 
    num_sorted = sorted(nums)
    num_small = [] 
    for i in num_sorted: 
        nums_final = len(num_sorted[num_sorted.index(i)+1:])
        num_small.append(nums_final)
    # print(num_sorted[1:])
    return(num_small)
    #return(num_sorted)
            



#### A recursive function:

# A function that calls itself!
### Base Case: when the master function call should stop!



# def count(x):
#   print('X: ', x)
#   if x == 1:
#     return x
#   else:
#     return count(x-1)

# count(10)

# 10, n-1, n-1, n-1


def recursive_sum(n):
  if n == 1:
    return 1
  else:
    return n + recursive_sum(n-1)


#print(recursive_sum(10))
# 10 + 9 + 8 + 7.... + 1

### Factorial function:
# 6!
# 6 x 5 x 4 x 3 x 2 x 1



def factorial(n): 
  if n == 1: 
    return 1 
  else: 
    return n * factorial(n-1)

# print(factorial(6))


#import math as ma
#print(ma.factorial(6))

def factorial(n): 
  sum_factorial  = 1
  for i in range(1, n+1): 
    sum_factorial *= i 
  return(sum_factorial)

#print(factorial(6))



#import math as ma
#print(dir(ma))


#### Solved with a while loop?

def factorial(n): 
  sum_factorial = 1
  while n != 1: 
    sum_factorial *= n 
    n = n - 1 
  return(sum_factorial)
   
#print(factorial(6))


#####
# Reduces a sequence to a single value
# A function which accepts two values, and returns one

# ADD: x,y: x+y

# 10,5,4,3,2
# 15,4,3,2
# 19,3,2
# 22,2
# 24

from functools import reduce

#### Give me any list of nums:
#### Add function, takes 2 nums and returns the sum.

ls = [1,2,3,4]

def add(x,y): 
  return(x+y) 

### reduce(func, sequence)

#print(reduce(add,ls))

##### Reversing a string with reduce?

city = 'London'

def city_func(a,b):
  return(b+a)

#print(reduce(city_func, city))


# L, o, n, d, o, n
# oL, n, d,  o,  n
# noL, d, o, n
# dnoL, o, n
# odnoL, n
# nodnoL

city = 'London'


#for i in range(len(city)-1):
#  print(city[i], city[i+1])


# def tester(*a):
#   for i in a:
#     print('Hi!', i)

# tester('onetwo', 'yes', 'no')



#### Node Class:
# Node has 3 attributes:
# Left - Initially set to None
# Right - Initially set to None
# Data - Required at runtime!


class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data


x = Node(10)
y = Node(100)
z = Node(1)


x.left = y
x.right = z



