class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashSet = set()
        # for num in nums:
        #     if num in hashSet:
        #         return True
        #     else:
        #         hashSet.add(num)
        # return False
        if (len(nums) != len(set(nums))):
            return True
        else:
            return False