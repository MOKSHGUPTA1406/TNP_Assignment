from typing import List

def self_product(nums: List)->List:
    ans=[1]*len(nums)
    left=1
    for x in range(len(nums)):
        ans[x]*=left
        left*=nums[x]
    right=1
    for x in range(len(nums)-1,-1,-1):
        ans[x]*=right
        right*=nums[x]
    return ans

print(self_product(nums=[1,2,3,4]))