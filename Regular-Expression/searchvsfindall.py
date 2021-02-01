#Jedsada Luengaramsuk jedsada-io
#1 Febuary 2021

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
mo.group()
#'415-555-9999' will be shown because it's a first matched


#This is when I use findall instead
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
#['415-555-9999', '212-555-0000'] This will post all the searches
