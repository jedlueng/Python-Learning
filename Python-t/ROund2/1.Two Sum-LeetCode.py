l1= [3,3]
l2 = 6

def twoSum(nums , target):
    for i in nums:
        for e in nums:
            if nums.index(i) != nums.index(e) and i+e == target:
                return (nums.index(i),nums.index(e)) 

        
twoSum(nums=l1,target=l2) 




