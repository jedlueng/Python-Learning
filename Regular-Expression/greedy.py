#Jedsada Luengaramsuk jedsada-io
#1 Febuary 2021

#Regex object that find 3Ha or 5Ha
greedyHaRegex = re.compile(r'(Ha){3,5}'')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo1.group()
#This will show HaHaHaHaHa because it proitize 5 instead of 3



#Search for nongreedy(Smaller) instead
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group()
#HaHaHa This one prioritize the smaller one
