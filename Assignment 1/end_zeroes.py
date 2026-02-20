from typing import List

def zero(nums: List)->List:
    j=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[j]=nums[i]
            j+=1
    while(j<len(nums)):
        nums[j]=0
        j+=1
    return nums

print(zero(nums=[1,0,0,2,3,0,0,4]))