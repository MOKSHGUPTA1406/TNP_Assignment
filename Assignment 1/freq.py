from typing import List,Dict

def countfreq(nums: List)->Dict:
    if len(nums)==0: return {}
    freq=dict()
    for x in range(len(nums)):
        if nums[x] not in freq:
            freq[nums[x]]=1
            continue
        freq[nums[x]]+=1
    return freq

print(countfreq([1,1,1,1,1,2,2,3,4,5,5,2,2]))