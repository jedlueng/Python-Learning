import re

def numJewelsInStones(jewels, stones):
        #How many stone are also jewels
        #Case sensitive 
    jewels2 = [] 
    for i in jewels: 
        jewels2.append(i)
        jewels2.append('|')
    jewelsRegex = re.compile(r'{}'.format(jewels2))
    mo = len(jewelsRegex.findall(stones))
    return(mo)

m1 = 'aA' 
m2 = 'aAAbbbb'

#print(numJewelsInStones(m1,m2))


def numJewelsInStones(jewels: str, stones: str) -> int:
    jcount = 0
    for i in stones: # O(n)
        if i in jewels: # O(n)
            jcount += 1
    return(jcount)


#print(numJewelsInStones('aA', 'aAAbbbb'))


##### Asymptotic Notation
#### O(1) math operation, assinging vars, printing, if/elif/else
#### O(n) For loops, membership checks, lst.index(), lst.count()
##### Add up all lines, drop the smallest terms


lst = list(range(1000))

count = 0 # O(1)
for i in lst: # O(n)
  if i > 50 and i % 5 == 0: # O(1)
    count += 1 # O(1)

# Total = O(n) + O(3) ===> O(n)





def smallerNumbersThanCurrent(nums): 
    num_sorted = sorted(nums, reverse=True)
    return(num_sorted)
            
#len([num_sorted.index(i):])
 

num1 = [6,5,4,8]

#print(smallerNumbersThanCurrent(num1))

###### Brute Force:
# keep an empty array,
# For each number (i): Iterate through again, count Numbers (j) < (i)
# Append count to empty array



############################################

### Object Orientation

### A Class defines all the behaviours, actions and attributes about 'something'
### A Class is a template, we use this to make 'instances'

# a,b,c are 3 unique instances of the list class
a = [1,2,4]
b = [6,7,8]
c = [9,8,7]

#print(dir(a))
# dir() shows all attributes of the instances
# Regular methods -> Called on the instance
# Special methods -> Called by operators and built-in funcs.

#def __init__ (self,):

# __len__ -> Returns list size


#print(len(a)) # -> Calls __len__
#print(a) # -> calls __str__
# __iter__ -> Used by 'for' loops
# __eq__, __gt__, __lt__, __ge__, __le__

# x > y



def lenn(item):
  try:
    return(item.__len__())
  except:
    return('Object -{}- has no len!'.format(type(item).__name__))



#print(lenn(a))
#print(lenn(10))

a,b = 10,20
#print(a > b)
#print(a.__gt__(b))



#### Class to represent a 2d shape
### 2 attributes, height and width
### 2 methods, area and perimeter

##### Every Object comes the same base object
#### base Object class 

# a = object()
# print(dir(a))



class Shape: 
  def __init__(self, height, width): 
    self.height = height 
    self.width = width 

  def __str__(self):
    '''Called by the print function!'''
    return 'Hello!'


  def area(self): 
    return(self.height * self.width)
  
  
  def perimeter(self): 
    return(2 * self.height + 2 * self.width)

  def change_height(self, new_height):
    if isinstance(new_height, (int, float)):
      self.height = new_height


  def change_length(self,new_length):
    if isinstance(new_length, (int,float)): 
      if new_length < self.height + 10 and new_length > self.height -10: 
        self.length = new_length 




#### Change Length -> Length must be -10 or +10 different to height



house = Shape(10,10)
# house.height = 20
# house.width += 1
# print(house.height)
# house.change_height(105)
# print(house.height)

#print(house.area())
#print(house.perimeter())
#print(dir(house))


x = 10

y = -5

print(abs(x - y), abs(y - x))
print(x - y, y - x)



