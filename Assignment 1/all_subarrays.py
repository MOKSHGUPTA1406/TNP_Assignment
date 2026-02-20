from typing import List

def subarrays(nums: List)->List:
    ans=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)+1):
            ans.append(nums[i:j])
    return ans

print(subarrays([1,2,77,-5,44]))
