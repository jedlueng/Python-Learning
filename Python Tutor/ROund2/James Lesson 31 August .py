#https://projecteuler.net/problem=1
#By Jedlueng 29 August 2021

import timeit



"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""


# code1 = '''
# natural = 0
# for i in range(1,100000):
#     if i % 3 == 0 or i % 5 == 0:
#         natural += i  

# '''


# code_run_1 = timeit.timeit(stmt=code1, number=100)
# print('Code Took', code_run_1)


# code2 = '''
# lc2 = sum([i for i in range(1,100000) if i %3 == 0 or i % 5 == 0])
# '''


# code_run_2 = timeit.timeit(stmt=code2, number=100)
# print('Code 2 Took', code_run_2)





#Problem 6
#https://projecteuler.net/problem=6
#by Jedlueng 29 Aug 2021 

#sum of square 
sumofsquare = 0 
sumofh = 0 
for i in range(1, 101): 
    sumofsquare += i*i 
    sumofh += i 

sumofhsquare = sumofh ** 2


difference = sumofhsquare - sumofsquare


#print(difference)


def check_string_len(st1: str, st2: str) -> bool:
  '''Returns True if strings are of equal size'''
  return len(st1) == len(st2)

# print(check_string_len('abc', 'xxx'))
# print(check_string_len.__doc__)
# print(check_string_len.__annotations__)



# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
        

def twoSum(nums, target):
  pass
        



a = '123.543.34.12'
new_ip = ''


for i in a:
  if i != '.': 
    new_ip += i
  else: 
    new_ip += '[.]'

#print(new_ip)

#######################################
### map, filter, reduce

# given a sequence (list, tuple, dict...)
# Given a function 
# Process an entire sequence by passing it through the function



def add_1(x):
  return x + 1


nums = [1,2,3,4,5]
new_nums = []

for i in nums:
  new_number = add_1(i)
  new_nums.append(new_number)


#print(nums, new_nums)


## var = list(map(function, sequence))
new_nums = list(map(add_1, nums))
#print(new_nums)


numbers = [12,24,55,66,77,32,45,3]

#### A new list, y
## Which contans all numbers from x
## If the number is even, we half it
## if the number is odd, we square it

def eo (x):
  if x % 2 == 0:
    return x / 2 
  return x ** 2


y = list(map(eo,numbers))
#print(y)



######### Filter

# Function should have a bool output


##### var = list(filter(func, sequence))


def over_40(x):
  return x > 40

larger_nums = list(filter(over_40, numbers))
#print(larger_nums)


#### Even numbers, above 30


def e30 (x):
  if x %2 == 0 and x > 30: 
    return True
  return(False)

even_above_30 = list(filter(e30,numbers))
# print(even_above_30)

###################

### Prime Finding
# https://projecteuler.net/problem=7

# How can you do this quickly??



###### Power Digit sum
# https://projecteuler.net/problem=16


    
######
# https://leetcode.com/problems/two-sum/


# Brute force approach - easy, but slow!
# Can you do better than the brute force approach?


##### Time Complexity
# https://www.youtube.com/watch?v=D6xkbGLQesk
