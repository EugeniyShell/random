class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations

        result = [[]]
        for i in range(1, len(nums) + 1):
            result += [x for x in combinations(nums, i)]
        return [list(x) for x in result]