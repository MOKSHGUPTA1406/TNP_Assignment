from typing import List

def subsum(nums: List, target: int)->List:
    sum=0
    ans=[]
    i=0
    for x in nums:
        sum+=x
        ans.append(x)
        while sum>target:
            sum-=nums[i]
            ans.remove(nums[i]) 
            i+=1
        if sum==target:
            return ans
        

print(subsum([1,2,3,4,5,5],10))