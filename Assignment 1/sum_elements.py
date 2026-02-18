'''Sum of elements when array contains random elements'''

from typing import List

def ransum(nums: List)->int:
    if len(nums)==0: return 0
    sum=nums[0]
    for x in range(1,len(nums)):
        sum+=nums[x]
    return sum

print(ransum([1,2,3,4,5]))

'''Sum of elements when array contains 1 to n numbers'''

def setsum(nums: List)->int:
    return (len(nums)*(len(nums)+1))//2

print(setsum([1,2,3,4,5]))
