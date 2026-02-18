from typing import List

def remove_element(nums: List,target:int)->List:
    if len(nums)==0: return []
    x=0
    while nums[x]!=target and x<len(nums):
        x+=1
    if x==len(nums):
        return nums
    while(x<len(nums)-1):
        nums[x]=nums[x+1]
        x+=1
    nums.pop()
    return nums

print(remove_element([1,2,3,4,5,9],2))