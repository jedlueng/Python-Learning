#Jedsada LUengaramsuk jedsada-io
#Date: 2 Febuary 2021

import re


#This is everything excluding newline
noNewLineRegex = re.compile('.*')
noNewLineRegex.search('Serve the public trust. \nProtect the innocent. \mUphold the law.').group()

#'Serve the public trust'





#This is everything including newline
#re.DOTALL
noNewLineRegex = re,compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent.
\nUphold the law.').group()

#'Serve the public trust.\nProtect the innocent.\nUphold the law.'
