from typing import List

def leader_elements(nums: List)->List:
    if len(nums)==0: return []
    mx=nums[len(nums)-1]
    ans=[mx]
    for x in range(len(nums)-2,-1,-1):
        if mx<nums[x]:
            mx=nums[x]
            ans.append(mx)
    ans.sort(reverse=True)
    return ans

print(leader_elements([1,2,77,-5,44]))
