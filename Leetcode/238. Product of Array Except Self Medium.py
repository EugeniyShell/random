'''class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from functools import reduce

        if nums.count(0) >= 2:
            return [0 for _ in nums]
        elif nums.count(0) == 1:
            y = reduce(lambda x,y : x*y or x, nums)
            return [0 if x != 0 else y for x in nums]
        else:
            y = reduce(lambda x,y : x*y, nums)
            return [y//x for x in nums]'''


class Solution:
    def productExceptSelf(self, nums):
        t1 = [1] + list(accumulate(nums, mul))[:-1]
        t2 = list(accumulate(nums[::-1], mul))[::-1][1:] + [1]
        return [x * y for x, y in zip(t1, t2)]