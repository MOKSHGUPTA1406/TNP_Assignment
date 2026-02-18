from typing import List

def dup(nums: List)->int:
    if len(nums)==0: return []
    freq=[0]*(max(nums)+1)
    ans=[]
    for x in range(len(nums)):
        freq[nums[x]]+=1
        if freq[nums[x]] not in ans:
            if freq[nums[x]]>1:
                ans.append(nums[x])
    return ans

print(dup([1,2,3,4,3,2,5,7]))