# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
#Jedlueng 7 September 2021

def smallerNumbersThanCurrent(nums): 
    num_sorted = sorted(nums, reverse=True)
    return(num_sorted)
            
len([num_sorted.index(i):])
 

num1 = [6,5,4,8]

print(smallerNumbersThanCurrent(num1))

###### Brute Force:
# keep an empty array,
# For each number (i): Iterate through again, count Numbers (j) < (i)
# Append count to empty array