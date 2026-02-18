from typing import List

def minmax(nums: List)->List:
    if len(nums)==0: return []
    mx=nums[0]
    mn=nums[0]
    for x in range(1,len(nums)):
        if mx<nums[x]:
            mx=nums[x]
            continue
        if mn>nums[x]:
            mn=nums[x]
    return [mx,mn]

print(minmax([1,2,77,44,-5]))
