from collections import defaultdict


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        left = 0
        right = 0
        d = defaultdict(int)
        substr = ""
        d2 = defaultdict(int)
        for right in range(len(s)):
            substr += s[right]
            d2[s[right]] += 1
            if (right - left + 1) < minSize:
                # right += 1
                continue
            if len(d2) <= maxLetters:
                d[substr] += 1

            d2[s[left]] -= 1
            if not d2[s[left]]:
                del d2[s[left]]
            left += 1
            substr = substr[1:]
        if d:
            return max(d.values())
        else:
            return 0
