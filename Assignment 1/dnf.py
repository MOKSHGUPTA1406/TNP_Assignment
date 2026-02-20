from typing import List

def swap(nums: List, n1: int, n2: int)-> List:
    temp=nums[n1]
    nums[n1]=nums[n2]
    nums[n2]=temp
    return nums

def dnf_sort(nums: List)->list:
    if len(nums)==0: return []
    low=0
    mid=0
    high=len(nums)-1
    while(mid<=high):
        if nums[mid]==0:
            swap(nums,low,mid)
            low+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
        else:
            swap(nums,mid,high)
            high-=1
    return nums

print(dnf_sort([1,0,0,2,0,0,1,1,2]))