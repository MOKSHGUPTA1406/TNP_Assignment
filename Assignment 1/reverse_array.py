from typing import List

def reverse(nums: List)->List:
    if len(nums)==0: return []
    for x in range(len(nums)//2):
        temp=nums[x]
        nums[x]=nums[len(nums)-x-1]
        nums[len(nums)-x-1]=temp
    return nums

print(reverse([1,2,3,4,5,9]))