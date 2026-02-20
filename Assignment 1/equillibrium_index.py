from typing import List

def equilibrium(nums: List)->int:
    if len(nums)==0: return -1
    lsum=0
    rsum=0
    for x in nums:
        lsum+=x
    for x in range(1,len(nums)):
        rsum+=nums[x-1]
        lsum-=nums[x-1]
        if rsum==lsum-nums[x]:
            return x
    return -1

print(equilibrium(nums=[14,2,4,3,2,4,1]))