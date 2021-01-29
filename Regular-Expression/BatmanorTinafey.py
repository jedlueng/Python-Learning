#Jedsada Luengaramsuk (jedsada.io)
#Date: 28 January 2021

#Regex object match either Batman or Tina Fey
heroRegex = re.compile(r'Batman|Tina Fey)

#matching object 1
mo1 = heroRegex.search('Batman and Tina Fey.')

mo.group()
#This will show 'Batman' because it see Batman before Tina BatmanorTinafey

mo2 = heroRegex.search('Tina Fey and Batman.')
mo2.group()
#This will show Tina Fey.
