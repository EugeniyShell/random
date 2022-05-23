class Solution:
    """Extremly not optimal"""
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #from itertools import combinations

        def getNext(pos, step, arr):
            while True:
                try:
                    if arr[pos] != arr[pos+step]:
                        return pos + step
                except IndexError:
                    return pos + step
                pos = pos + step

        result = []
        if len(nums) < 3:
            return result
        nums = sorted(nums, key=lambda i: abs(i))
        zero = nums.count(0)
        if zero > 2:
            result.append([0,0,0])
        if zero > 0:
            arr = set(nums[zero:])
            arr = sorted(arr, key=lambda i: abs(i))
            for i in range(len(arr)-1):
                if arr[i] + arr[i+1] == 0:
                    result.append([0, arr[i], arr[i+1]])
                    i += 1
        neg = [i for i in nums if i < 0]
        pos = [i for i in nums if i > 0]
        i = 0
        while i < len(neg):
            x, y = 0, len(pos)-1
            while x < y:
                if pos[x] + pos[y] + neg[i] == 0:
                    result.append([neg[i], pos[x], pos[y]])
                    x = getNext(x, 1, pos)
                    y = getNext(y, -1, pos)
                elif pos[x] + pos[y] + neg[i] > 0:
                    y = getNext(y, -1, pos)
                elif pos[x] + pos[y] + neg[i] < 0:
                    x = getNext(x, 1, pos)
            i = getNext(i, 1, neg)
        i = 0
        while i < len(pos):
            x, y = 0, len(neg)-1
            while x < y:
                if neg[x] + neg[y] + pos[i] == 0:
                    result.append([pos[i], neg[x], neg[y]])
                    x = getNext(x, 1, neg)
                    y = getNext(y, -1, neg)
                elif neg[x] + neg[y] + pos[i] < 0:
                    y = getNext(y, -1, neg)
                elif neg[x] + neg[y] + pos[i] > 0:
                    x = getNext(x, 1, neg)
            i = getNext(i, 1, pos)
        return result
