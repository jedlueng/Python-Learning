#Jedsada LUEGNARAMSUK jedsada-io
#2 Febuary 2021

import re

#Match everything in a non greedy way
nongreedyRegex = re,compile(r'<.*?>'')

mo = nongreedyRegex.search('<To serve man> for dinner.>')

mo.group()
#'<To serve man> for dinner.>'
