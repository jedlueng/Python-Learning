#Jedsada Luengaramsuk Jedsada-io
#Date: 27 January 2021
#Source Automated boring stuff with Python textbook
#Find the pattern num/num/num/-/num/num/num/-/num/num/num
def isPhoneNumber(text):
    #If text is not equal 12 return False
    if len(text) != 12:
        return False
    #If text[0:3] is not a decimal return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    #If text[3] is not '-' return false
    if text[3] != '-':
        return False
    #If text[4:7] is not a decimal return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    #If text[7] is not equal to '-' return False
    if text[7] != '-':
        return False
    #If text[8:12] is not decimal return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))


#Output
#415-555-4242 is a phone number:
#True
#Moshi moshi is a phone number:
#False
