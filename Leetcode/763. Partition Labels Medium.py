class Solution:
    def partitionLabels(self, s: str):
        """res = 0
        ans = list()
        pointer = s.rfind(s[res])
        while sum(ans) != len(s):
            if res == pointer:
                ans.append(pointer - sum(ans) + 1)
                res += 1
                if res > len(s)-1:
                    break
                else:
                    pointer = s.rfind(s[res])
            else:
                if s.rfind(s[res]) > pointer:
                    pointer = s.rfind(s[res])
                    res += 1
                elif s.rfind(s[res]) <= pointer:
                    res += 1
        return ans"""

        last = {c: i for i, c in enumerate(s)}
        res = end = 0
        ans = []
        for i, c in enumerate(s):
            res = max(res, last[c])
            if i == res:
                ans.append(i - end + 1)
                end = i + 1
        return ans