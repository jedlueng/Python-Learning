#Jedsada Luengaramsuk jedsada-io
#2 Febuary 2021

import re

#regex object start with Hello
beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search('Hello world!')
#This will matched the string

#However this will not matched
beginsWithHello.search('He said hello.') == None





#This is the regex object that end with number
endsWithNumber = re.compile(r'\d$')

#This will matched
endsWithNumber.search('Your number is 42')

endsWithNumber.search('Your number is forty two.') == None
#This will return true


#Regex that both begin and end with one or more num Characters
#With one or more num chars
wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567890')
#This one will match

#This one won't because it's contain chars
wholeStringIsNum.search('12345xyz67890') == None

#This one won't because it contain space
wholeStringIsNum.search('12 34567890') == None
