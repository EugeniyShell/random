class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter

        base_counter = Counter(words)
        len_list = len(words)
        len_word = len(words[0])
        result = []

        for a in range(len_word):
            for b in range(a, len(s) - len_list * len_word + 1, len_word):
                if b in result:
                    continue
                if base_counter[s[b:b + len_word]]:
                    copy_counter = base_counter.copy()
                    copy_counter[s[b:b + len_word]] -= 1
                    flag = False
                    for c in range(1, len_list):
                        if copy_counter[s[b + c * len_word:b + (c + 1) * len_word]]:
                            copy_counter[s[b + c * len_word:b + (c + 1) * len_word]] -= 1
                        else:
                            flag = True
                            break
                    if not flag:
                        result.append(b)
                        for d in range(b + len_word * len_list, len(s) - len_word + 1, len_word):
                            if s[b:b + len_word] == s[d:d + len_word]:
                                b = b + len_word
                                result.append(b)
                            else:
                                break
        result.sort()
        return result
