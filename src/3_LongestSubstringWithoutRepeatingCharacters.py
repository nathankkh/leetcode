class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        curr = set()
        for right in range(len(s)):
            # when duplicate is found, shorten window until the original instance of 
            # right is no longer part of the window
            while s[right] in curr:
                curr.remove(s[left])
                left += 1
            
            curr.add(s[right])
            res = max(res, right - left + 1)
        
        return res
