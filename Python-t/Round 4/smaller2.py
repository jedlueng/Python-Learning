#12 Sep by Jedlueng 
#With strategy from Youtuber and my own code 
def smallerNumbersThanCurrent(nums): 
    num_dict = {} 
    nums_sorted = sorted(nums)
    nums_2 = [] 
    for i in nums_sorted:
        num_dict[i] = nums_sorted.index(i)
    for i in nums: 
        nums_2.append(num_dict[i])
    return(nums_2)







    #return(num_sorted)


num1 = [6,5,4,8]

print(smallerNumbersThanCurrent(num1))
