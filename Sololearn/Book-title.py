#Jedlueng 
#17 September 2021
#Fix it one by one using built in method 

file = open("/usercode/files/books.txt", "r")
#your code goes here

for i in file:
    strip_i = i.strip('\n')
    list_i = list(strip_i)
    print(str(list_i[0])+str(len(list_i)))
file.close()