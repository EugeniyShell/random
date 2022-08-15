class Solution:
    """def maxDistToClosest(self, seats: List[int]) -> int:
        ans = 0
        sflag = 0
        eflag = 0
        if seats[0] == 0:
            sflag = 1
        if seats[-1] == 0:
            eflag = 1
        temp = 0
        for i in range(len(seats)):
            if seats[i] == 0:
                temp += 1
            else:
                if temp == 0:
                        continue
                if sflag:
                    ans = max(ans, temp)
                    temp = 0
                    sflag = 0
                else:
                    ans = max(ans, (temp+1)//2)
                    temp = 0
        if eflag:
            ans = max(ans, temp)
        return ans"""

    def maxDistToClosest(self, seats):
        ans = seats.index(1)
        seats.reverse()
        ans = max(ans, seats.index(1))
        for seat, group in itertools.groupby(seats):
            if not seat:
                K = len(list(group))
                ans = max(ans, (K + 1) // 2)

        return ans