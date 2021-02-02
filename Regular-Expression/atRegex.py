#Jedsada LUENGARAMSUK jedsada-io
#Date: 2 Febuary 2021

import re

atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')
#All matched because it's not newline chars
