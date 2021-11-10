#Jedlueng 31 August 2021
'''215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?'''

two_times_1000 = 2 ** 1000
two_times_1000_read = (two_times_1000)


list_21000 = list(map(int, str(two_times_1000)))

print(sum(list_21000))



#for i in two_times_1000: 
    #list_of_num.append[i]

#sum_list_of_num = sum(list_of_num)

#print(sum_list_of_num)