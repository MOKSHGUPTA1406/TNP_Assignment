from typing import List

def peak_ele(nums: List)->int:
    if len(nums)==0: return -1
    if nums[0]>nums[1]: return nums[0]
    for x in range(1,len(nums)-1):
        if nums[x-1]<nums[x] and nums[x]>nums[x+1]:
            return nums[x]
    return nums[len(nums)-1]

print(peak_ele([5,2,3,10,3,2,5,7]))