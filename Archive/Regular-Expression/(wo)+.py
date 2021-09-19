#Created by Jedsada Luengaramsuk
#Date: 31 January 2021

#Regex object match one or more on (wo)
batRegex = re.compile(r'Bat(wo)+man')

mo1= batRegex.search('The Adventures of Batwoman')
mo1.group()
#This will show Batwoman because it appear in the text

mo2 = batRegex.search('The Adventures of Batwowowowoman')
mo.group()
#THis will show Batwowowowoman because it appear more than one time\

mo3 = batRegex.search('The Adventures of Batman')
mo3 == None
#This won't appear because (wo) does not appear in this text.
