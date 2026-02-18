from typing import List

def check(nums: List)->bool:
    if len(nums)==0: return True
    for x in range(len(nums)-1):
        if nums[x]>nums[x+1]: return False
    return True

print(check([1,2,3,7,4,5,9]))