from typing import List

def merge_arrays(nums1: List,nums2:List)->List:
    i=0
    j=0
    ans=[]
    while(i<len(nums1) and j<len(nums2)):
        if(nums1[i]<nums2[j]):
            ans.append(nums1[i])
            i+=1
            continue
        if(nums1[i]>nums2[j]):
            ans.append(nums2[j])
            j+=1
            continue
        if(nums1[i]==nums2[j]):
            ans.append(nums1[i])
            i+=1
            j+=1
            continue
    while(i<len(nums1)):
        ans.append(nums1[i])
        i+=1
    while(j<len(nums2)):
        ans.append(nums2[j])
        j+=1
    return ans
            
        
nums1=[1,2,4,7,9,10,11]
nums2=[1,3,5,8]
print(merge_arrays(nums1,nums2))