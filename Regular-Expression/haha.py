#Jedsada Luengaramsuk jedsada-io
import re


#Create regex object. Search for hahaha
haRegex = re.compile(r'(ha){3}')

mo1=haRegex.search('HaHaHa')
mo1.group()
#Show HaHaHa (Perfect matched)

mo2 = haRegex.search('Ha')
mo2 = None
#Return True

#Summary
#()is for the text {} is for the number of times it must appear
