#Jedsada Luengaramsuk (jedsada-io)
#27 January 2021

#import re module to start using regular expression
import re

#Step 1 create a regex object

#Passing string representation of regular expression to re.compile()
#This is the string representation for 3nums+dash+3nums+dash+4nums
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')



#Step 2 Matching Regex Objects
#search() method searches the string that match with regex object
mo = phineNumRegex.search('My number is 415-555-4242')
print('Phone number found: ' + mo.group())

#Output
#Phone number found: 415-555-4242
