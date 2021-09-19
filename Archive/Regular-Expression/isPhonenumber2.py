#Jedsada Luengaramsuk (jedsada-io)
#Date: 27 January 2021
#This program check whether a message have a number
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    #This loop is running one by one to check the number
    #If the condition is met, it will print Phone number found: + chunk
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')
