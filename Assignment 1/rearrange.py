from typing import List

def alternate(nums: List)->List:
    nums.sort()
    ans=[]
    i=0
    j=len(nums)-1
    while(i<=j):
        if i==j:
            ans.append(nums[j])
            break
        ans.append(nums[j])
        ans.append(nums[i])
        i+=1
        j-=1
    return ans

print(alternate([1,2,77,-5,44]))
