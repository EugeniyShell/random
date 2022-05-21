class Solution:
    """2 variants - use set and use in-place substitution for negative values"""
    def firstMissingPositive(self, nums: List[int]) -> int:
        """ans = set(nums)
        i = 1
        while i in ans:
            i += 1
        return i"""

        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = len(nums) + 1

        for num in nums:
            num = abs(num)
            if num <= len(nums):
                nums[num - 1] = abs(nums[num - 1])
                nums[num - 1] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return len(nums) + 1
