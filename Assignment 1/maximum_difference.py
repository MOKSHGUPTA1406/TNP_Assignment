from typing import List
import math
def diff(nums: List)->List:
    ans=-math.inf
    m=nums[0]
    for x in range(1,len(nums)):
        if nums[x]-m>ans:
            ans=nums[x]-m
        if m>nums[x]:
            m=nums[x]
    return ans

print(diff(nums=[10,2,3,4]))