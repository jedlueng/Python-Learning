#Problem 6
#https://projecteuler.net/problem=6
#by Jedlueng 29 Aug 2021 

#sum of square 
sumofsquare = 0 
for i in range(1, 101): 
    sumofsquare += i**i 


#sum of the squares of the first one hundred
sumofh = 0 
for i in range(1,101): 
    sumofh += i 

sumofhsquare = sumofh ** sumofh 


difference = sumofhsquare - sumofsquare

print(difference)