#Jedsada Luengaramsuk (jedsada-io)
#Date: 28 January 2021

import re

#Create regex objectg
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')


mo.group(1)
#This will show group one (\d\d\d)

mo.group(2)
#This will show group 2 (\d\d\d\d)

mo.group(0)
#This will show no group(\d\d\d)-(\d\d\d-\d\d\d\d)

mo.group()
#This will show no group the same as mo.group(0)

mo.groups()
#This will retrive all the groups ('group1','group2')


areaCode, mainNumber = mo.groups()
#This will name areaCode group1, name mainNumber group2
print(areaCode)
#This will print group1
print(mainNumber)
#This will print group2
