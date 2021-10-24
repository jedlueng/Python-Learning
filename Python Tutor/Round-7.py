#17 September 2021 
# txt = input()

# #your code goes here

# txt_ls = txt.split(' ')
# txt_ls_dict = {}
# txt_ls_len = [] 
# for word in txt_ls: 
# 	txt_ls_dict[word] = len(word)
# 	txt_ls_len.append(len(word))

# for key, value in txt_ls_dict.items():
#     if value == max(txt_ls_len):
#         print(key)


# #print(sorted(txt_ls, key=len)[-1])
# print(txt_ls_dict)
# d = {i: len(i) for i in txt_ls}
# print(d)


# x = {i : i**2 for i in range(1,6) if i % 2 == 0}
# print(x)


### Generator
###import timeit



code1 = '''
import math as ma
factorials = [ma.factorial(i) for i in range(1,2000)]
'''

code2 = '''
import math as ma
factorials_gen = (ma.factorial(i) for i in range(1,2000000))
'''

#print(timeit.timeit(stmt=code1, number=10))
#print(timeit.timeit(stmt=code2, number=10))


d = [1,2,3,4,5]

def add(i):
  return i + 1

d_new = list(map(add, d))
d_new = list(map(lambda x : x+1, d))

# print(d_new)


# d = 'A'
# print(d * 10)


names = ['James', 'Alex', 'Matthew', 'Charlotte', 'Daniel']
## First character multiplied by its len
### Create the function for the single case
### use map(func, names)

def multi_name(name): 
  return(name[0]* len(name))

#print(list(map(multi_name,names)))


print(list(map(lambda x : x[0] * len(x), names)))



#### Reverse each name, keep the relative order of the list

def reverse(name): 
  return(name[::-1])

#print(list(map(reverse,names)))


#print(list(map(lambda x : x[::-1], names[::-1])))


a = ['a1', 'b5', 'a9', 'b3', 'a7']
### Sort a, sort by the numbers of each string

### list.sort(key=function)

#a.sort(key=lambda x: 
# int(x[1]))
#print(a)


### Lambda/Filter
## Lambda True/False


sentence = 'today is friday and the sun is out'

def is_vowel(a):
  '''Return True if a is a vowel'''
  return a.lower() in 'aeiou'


# sentence = ''.join(list(filter(is_vowel, sentence)))
# print(sentence)

#### Remove all spaces with function/filter

def no_space(word): 
  if word != ' ':
    return True

#lambda x : x > 5


# print(''.join(filter(no_space,sentence))) 
# print(''.join(list(filter(lambda x : x != ' ',sentence)))) 


sentence = 'today is saturday and the sun is out and the month is september'
# split, lambda, filter, join,

### Only want words that begin with s
def begin_s(word): 
  ls = [] 
  word_split = word.split(' ')
  for i in word_split: 
    if i[0] == 's':
      ls.append(i)
  return(ls)



#print(' '.join(filter(lambda a : a[0] == 's', sentence.split())))


### Running Subtraction
lst = [10,5,6,7,8,1,2]

from functools import reduce

### Function(a,b) -> single value

def reverse_sum(x,y): 
  return(x-y)

print(reduce(reverse_sum,lst))
print(reduce(lambda x,y : x - y ,lst))


def total(*a):
  return a


x = lambda *a : sum(a)

# print(x(1,2,4))


# print(total())
# print(total(1,2,3))
# print(total(1,1,1,1,1,1,1,1))


# def total(a,b,*c):
#   return a,b,c
# print(total(10,20, 5,5,5,5))


x = [1,2,3,4,5,6]

a, b, *c = x
print(a,b,c)