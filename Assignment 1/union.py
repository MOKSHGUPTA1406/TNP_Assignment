from typing import List

def uni(nums1: List,nums2:List)->List:
    ans=[]
    for x in nums1:
        if x not in ans:
            ans.append(x)
    for x in nums2:
        if x not in ans:
            ans.append(x)
    return ans
            
        
nums1=[1,2,3,4,7,9,10,11]
nums2=[1,3,5,8,9]
print(uni(nums1,nums2))