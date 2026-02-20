from typing import List
import math
def kadane_algo(nums: List)->int:
    if len(nums)==0: return []
    max_sum=-math.inf
    curr_sum=0
    for x in range(len(nums)):
        curr_sum+=nums[x]
        max_sum=max(curr_sum,max_sum)
        if curr_sum<0:
            curr_sum=0
    return max_sum

print(kadane_algo([-1,-2,77,-5,-44]))
