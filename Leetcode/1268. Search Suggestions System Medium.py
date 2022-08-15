class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans = []
        for x in range(1, len(searchWord)+1):
            temp = []
            count = 0
            for y in products:
                if y.startswith(searchWord[:x]) is True:
                    temp.append(y)
                    count += 1
                    if count == 3:
                        break
            ans.append(temp)
        return ans
