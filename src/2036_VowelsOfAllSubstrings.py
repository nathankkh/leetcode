class Solution:
    def countVowelsTLE(self, word: str) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        res = 0
        for i in range(len(word)):
            for j in range(i, len(word)):
                sub = word[i : j + 1]
                for c in sub:
                    if c in vowels:
                        res += 1

        return res

    def countVowels(self, word: str) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        res = 0
        for i in range(len(word)):
            if word[i] in vowels:
                res += (i + 1) * (len(word) - i)
        return res

    def countVowelsEnum(self, word: str) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        res, temp = 0, 0
        for i, ch in enumerate(word, 1):
            if ch in vowels:
                temp += i
            res += temp
        return res


tests = [["aba", 6], ["abc", 3], ["ltcd", 0]]
sol = Solution()
for test in tests:
    print(sol.countVowelsEnum(test[0]), test[1])
