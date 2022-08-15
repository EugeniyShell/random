class Solution:
    import itertools

    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        else:
            res = []
            for n in nums:
                new = nums.copy()
                # find all permutations ending in the current n:
                new.remove(n)
                ans = self.permute(new) # recurse, removing the current n from nums
                for item in ans:
                    item.append(n)
                res.extend(ans)
            return res