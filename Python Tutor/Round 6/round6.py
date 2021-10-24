


### Recursion:


#### Reverse a string using Recursion?


#### Non-Recursively (for loop?)


st = 'Hello'

# Iterate Backwards?
# list.insert(index, element)   
## .join()

#a = ['a', 'b', 'c']
#x = ''.join(a)

#print(x)

##### Logging
##### print
import logging

logging.basicConfig(filename='test.txt',
                    filemode='a',
                    level=logging.DEBUG)




def reverse_string(word): 
  reverse_ls = []
  for i in word:
    logging.info('Current List: {}'.format(reverse_ls))
    reverse_ls.insert(0,i)


  reverse_str = str(''.join(reverse_ls))
  logging.info('Current List_string: {}'.format(reverse_str))('Current List : {}'.format())
  
  return reverse_str 

#print(reverse_string(st))



def rev_string(st):
  ####
  logging.info('st {}'.format(st))
  if st == '':
    return st
  else:
    return rev_string(st[1:]) + st[0]

#### Recursively takes the 0th element, puts it on the right side

#print(rev_string('Hello'))

x = 'Apple'
x = x[::-1]
#print(x)

# Hello
# ello  H
# llo  eH
# lo  leH
#   olleH



a = 'England'
#[start:end:step]

# print(a[::2]) # Entire string, in steps of 2
# print(a[::-1]) # Entire string, in steps of -2
# Start, to end, in negative steps!


#### Map/Lambda
#### Filter/Lambda
#### Reduce/Lambda



a = [5,4,6,7,5,4,3]

#### Use map to double all these numbers?

def double(num):
  return num * 2


#print(list(map(double, a)))

### Using a blank list, for loop, and append?

# ls = [] 
# for i in a: 
#   ls.append(double(i)) # Function call here

# print(ls)

####### Given a, we only want numbers <= 5


def lessthanfive (num): 
  if num <= 5:
    return num 
  
#print(list(filter(lessthanfive,a)))


from functools import reduce

# Iteratively turns 2 elements into 1
# sum(a,b) -> a+b
# 5,8,2,10
# 13,2,10
# 15,10
# 25


x = [1,2,3,4,5]


def plus(num1,num2):
  return(num1 * num2)

#print(reduce(plus,x))

#### Reverse a string with reduce?

a = 'Hello'
# H, e

def re(word,word2): 
  return(word2+word)

#print(reduce(re,a))

# H,e,l,l,o
# ?

# H e > eH
# ll > lleH
# o > olleH 

#        inputs : outputs
x = lambda a,b : a+b

#print(x(100,200))


print(list(map(lambda x : x ** 2, [1,2,3,4,5])))

print(reduce(lambda a,b : b+a, 'Helloyes123'))