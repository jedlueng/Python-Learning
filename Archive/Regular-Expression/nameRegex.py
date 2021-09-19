#Jedsada Luengaramsuk jedsada-io
#2 Feb 2021
import re

#Regex object where matched First Name then everything except new line. Also the name as  last name
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)'')

mo = nameRegex.search('First Name: Jedsada Last Name: LUENGARAMSUK')

mo.group(1)
#Jedsada

mo.group(2)
#LUENGARAMSUK
