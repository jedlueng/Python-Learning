# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
#Jedlueng 7 September 2021
#Finished 12 September 2021 

def smallerNumbersThanCurrent(nums): 
    num_sorted = sorted(nums)
    num_small = [] 
    for i in num_sorted: 
        nums_final = len(num_sorted[num_sorted.index(i)+1:])
        num_small.append(nums_final)
    # print(num_sorted[1:])
    return(num_small)
    #return(num_sorted)
            


num1 = [6,5,4,8]

print(smallerNumbersThanCurrent(num1))

###### Brute Force:
# keep an empty array,
# For each number (i): Iterate through again, count Numbers (j) < (i)
# Append count to empty array