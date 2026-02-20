from typing import List

def longest_consecutive(nums: List)->int:
    ans=0
    count=1
    for x in range(len(nums)-1):
        if nums[x]+1==nums[x+1]:
            count+=1
            ans=max(count,ans)
        else:
            count=1
    return ans

print(longest_consecutive(nums=[1,2,3,5,6]))