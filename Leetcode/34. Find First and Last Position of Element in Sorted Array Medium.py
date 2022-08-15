class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        import bisect

        if not len(nums):
            return [-1, -1]
        ansl = bisect.bisect_left(nums, target)
        ansr = bisect.bisect_right(nums, target)
        if ansl != ansr:
            return [ansl, ansr - 1]
        else:
            return [-1, -1]