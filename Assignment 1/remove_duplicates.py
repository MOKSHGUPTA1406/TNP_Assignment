from typing import List

def rem_dup(nums: List)->List:
    if len(nums)==0: return []
    freq=[0]*(max(nums)+1)
    ans=[]
    for x in range(len(nums)):
        freq[nums[x]]+=1
        if freq[nums[x]]>1:
            continue
        ans.append(nums[x])
    return ans

print(rem_dup([1,1,1,2,2,4,4,3,3,3,5,9]))