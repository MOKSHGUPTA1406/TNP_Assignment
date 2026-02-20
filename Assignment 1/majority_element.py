from typing import List

def m_element(nums: List)->int:
    for x in nums:
        if nums.count(x)>len(nums)//2:
            return x
    return -1

print(m_element([1,1,1,2,2]))
