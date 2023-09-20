
#HashMap 利用哈希表的特性，当添加的key重复时，覆盖对应的value
class Solution1:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash={}
        for i in range(len(nums)):
            if(nums[i] not in hash):
                hash[nums[i]]=i
            else:
                if(i-hash[nums[i]]<=k):
                    return True
                else:
                    hash[nums[i]]=i
        return False