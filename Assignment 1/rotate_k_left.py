from typing import List

# 1,2,3,4,5   
# 4,5,1,2,3

def rotate_k_left_loop(nums: List, k: int)->List:
    if len(nums)==0: return []
    if k==0: return nums
    while(k>0):
        temp=nums[len(nums)-1]
        for x in range(len(nums)-1,0,-1):
            nums[x]=nums[x-1]
        nums[0]=temp
        k-=1
    return nums

print(rotate_k_left_loop([1,2,3,4,5,1,99],4))
# 4,5,1,99,1,2,3

def rotate_k_left_built(nums: List, k: int)->List:
    if len(nums)==0: return []
    if k==0: return nums
    while(k>0):
        temp=nums[len(nums)-1]
        nums.pop()
        nums.insert(0,temp)
        k-=1
    return nums

print(rotate_k_left_built([1,2,3,4,5,1,99],4))

def rotate_k_left_slice(nums: List, k: int)->List:
    if len(nums)==0: return []
    if k==0: return nums
    return nums[k-1:]+nums[:k-1]

print(rotate_k_left_slice([1,2,3,4,5,1,99],4))
