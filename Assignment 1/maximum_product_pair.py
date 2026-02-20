from typing import List
import math
def product(nums: List)->List:
    if len(nums)==0: return []
    smx=mx= -math.inf
    smn=mn= math.inf
    for x in range(len(nums)):
        if nums[x]>mx:
            smx=mx
            mx=nums[x]
        elif nums[x] > smx and nums[x] != mx:
            smx = nums[x]
    for x in range(len(nums)):
        if nums[x]<mn:
            smn=mn
            mn=nums[x]
        elif nums[x] < smn and nums[x] != mn:
            smn = nums[x]
    
    ans= [smn,mn] if mn*smn>mx*smx else [smx,mx]
    return ans

print(product(nums=[7,4,5,-8,-9]))