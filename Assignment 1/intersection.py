from typing import List

def intersect(nums1: List,nums2:List)->List:
    ans=[]
    for x in nums1:
        if x in nums2:
            ans.append(x)
    return ans
            
        
nums1=[1,2,3,4,7,9,10,11]
nums2=[1,3,5,8,9]
print(intersect(nums1,nums2))