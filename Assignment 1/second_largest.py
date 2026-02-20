from typing import List
import math
def second(nums: List)->int:
    if len(nums)==0: return []
    smx=mx= -math.inf
    for x in range(len(nums)):
        if nums[x]>mx:
            smx=mx
            mx=nums[x]
        elif nums[x] > smx and nums[x] != mx:
            smx = nums[x]
    return [smx,mx]

print(second([1,2,3,4,5,9]))