from typing import List

# 1,2,3,4,5   
# 3,4,5,1,2

def rotate_k_loop(nums: List, k: int)->List:
    if len(nums)==0: return []
    if k==0: return nums
    while(k>0):
        temp=nums[0]
        for x in range(len(nums)-1):
            nums[x]=nums[x+1]
        nums[len(nums)-1]=temp
        k-=1
    return nums

print(rotate_k_loop([1,2,3,4,5,1,99],4))

def rotate_k_built(nums: List, k: int)->List:
    if len(nums)==0: return []
    if k==0: return nums
    while(k>0):
        temp=nums[0]
        nums.remove(nums[0])
        nums.append(temp)
        k-=1
    return nums

print(rotate_k_built([1,2,3,4,5,1,99],4))

def rotate_k_slice(nums: List, k: int)->List:
    if len(nums)==0: return []
    if k==0: return nums
    return nums[k:]+nums[:k]

print(rotate_k_slice([1,2,3,4,5,1,99],4))
