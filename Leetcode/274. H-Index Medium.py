class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 1:
            return int(bool(citations[0]))
        citations.sort(reverse=True)
        for h in range(len(citations)):
            if h + 1 > citations[h]:
                return h
        return len(citations)