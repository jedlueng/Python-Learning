#Jedsada Luengaramsuk jedsada-io
#2 Febuary 2021

import re

#Regex object of one or more num , space then one or more word
xmasRegex = re.compile(r'\d+\s\w+'')


xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 m

#This will show all because it's fit the condition above
