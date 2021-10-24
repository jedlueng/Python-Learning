"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""


#Jedlueng 31 August 2021

prime = []

for num in range(1, 200000):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           prime.append(num)

print('I am running a program')
print('10001 prime number is', prime[10001])
print('Done!')

'''Output :
I am running a program
('10001 prime number is', 104759)
Done!
'''