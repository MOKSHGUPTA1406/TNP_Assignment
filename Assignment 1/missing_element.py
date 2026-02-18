from typing import List

def missing(nums: List)->int:
    if len(nums)==0: return []
    freq=[0]*(nums[len(nums)-1]+1)
    for x in range(len(nums)):
        freq[nums[x]]+=1
    for x in range(1,len(freq)):
        if freq[x]==0:
            return x
    return -1

print(missing([1,2,3,4,5,7]))