class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if j == i:
                    continue
                if self.isPrefixAndSuffix(words[i], words[j]):
                    count += 1
        return count

    def isPrefixAndSuffix(self, a, b):
        # returns True if *a* is a prefix & suffix of *b*
        l = len(a)
        if len(b) < len(a):
            return False
        if b[:l] == a and b[(len(b) - l):] == a:
            return True
        
        return False