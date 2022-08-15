class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        ans = 1
        for i in nums:
            if i - 1 not in nums:
                temp = i
                temp_ans = 1
                while temp + 1 in nums:
                    temp += 1
                    temp_ans += 1
                ans = max(ans, temp_ans)
        return ans