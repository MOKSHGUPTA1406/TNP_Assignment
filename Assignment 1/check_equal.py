from typing import List

def equal(nums1: List,nums2:List)->bool:
    if len(nums1)!= len(nums2): return False
    for x in nums1:
        if x not in nums2:
            return False
        if nums1.count(x)!=nums2.count(x):
            return False
    return True
            
        
nums1=[1,2,1,4]
nums2=[1,2,4,1]
print(equal(nums1,nums2))