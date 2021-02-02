#Jedsada Luengaramsuk jedsada-io
#2 Febuary 2021

import re

#Match all case

robocop = re.compile(r'robocop',re.I)
robocop.search('RoboCop is part man, part machine, all cop.').group()
#RoboCop

robocop.search('ROBOCOP protects the innocent.').group()
#ROBOCOP

robocop.search('Al, why does your programming book talk about robocop so much?').group()
#robocop
