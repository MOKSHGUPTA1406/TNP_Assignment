from typing import List

def target(nums: List,t: int)->List:
    if len(nums)==0: return []
    for x in range(len(nums)-1):
        for y in range(x, len(nums)):
            if nums[x]+nums[y]==t:
                return [nums[x],nums[y]]
    return []

print(target([0,1,2,13,4,5,9],6))