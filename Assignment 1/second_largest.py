from typing import List

def second(nums: List)->int:
    if len(nums)==0: return -1
    mx=nums[0]
    smx=mx
    for x in range(1,len(nums)):
        if nums[x]>mx:
            smx=mx
            mx=nums[x]
    return [mx,smx]

print(second([1,2,3,4,5,9]))