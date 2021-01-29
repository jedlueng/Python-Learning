#Jedsada Luengaramsu jedsada-io
#29 January 2021

#Create a regex object with ()?
batRegex = re.compile(r'Bat(wo)?man')


mo1 = batRegex.search('THe Adventures of Batman')


mo1.group()
#This will show Batman because Batman is founded in this text

mo2= batRegex.search('THe Adventures of Batwoman')
mo2.group()
#This one will show Batwoman because it's found.
