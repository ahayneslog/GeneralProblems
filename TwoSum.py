class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        history = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in history:
                return [history[remaining], i]
            history[v] = i
        return []

nums = [1,2,3,4,5]
target = 9

sln = Solution()
print(sln.twoSum(nums=nums, target=target))