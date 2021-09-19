#Jedsada LUengaramsuk jedsada-io
#29 January 2021

import re

#* mean match zero or more
batRegex = re.compile(r'Bat(wo)*man')

mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
#Batman

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
#Batwoman

mo3 = batRegex.search('The Adventures of Batwowowowoman')
#Batwowowwowoman
#This will match because of * match one or more.
