from typing import List

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7
        arr = []
        power = 0
        while n > 0:
            if n & 1:
                arr.append(2**power)
            n = n >> 1
            power += 1

        prefix = [1] * (power + 1)
        for i in range(len(arr)):
            prefix[i + 1] = prefix[i] * arr[i]
        print(prefix)

        answers = []
        for start, end in queries:
            if start == end:
                answers.append((prefix[end + 1] // prefix[end]) % mod)
            else:
                answers.append((prefix[end + 1] // prefix[start]) % mod)
        return answers
