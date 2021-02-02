#Jedsada Luengaramsuk jedsada-io
#2 Febuary 2021

import re

#regex object where match only aeiouAEIOU
consonantRegex =re.compile(r'[^aeiouAEIOU]')

consonantRegex.findall('RoboCop eats baby food. BABY FOOD')
#This will be matched
#['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', '', 'B', 'B', 'Y', ' ', 'F', 'D', '.']
