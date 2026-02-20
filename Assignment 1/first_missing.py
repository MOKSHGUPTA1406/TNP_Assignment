from typing import List

def miss(nums: List)->int:
    if len(nums)==0: return-1
    freq=[0]*(max(nums)+1)
    for x in range(len(nums)):
        freq[nums[x]]+=1
    for x in range(1,len(freq)):
        if freq[x]==0:
            return x
    return -1

print(miss([1,2,3,4,6]))