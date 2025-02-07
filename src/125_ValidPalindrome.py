class Solution(object):
    def isPalindrome(self, s: str):
        """
        :type s: str
        :rtype: bool
        """

        s = s.lower()

        arr = [c for c in s if (ord(c) <= 122 and ord(c) >= 97) or (ord(c) >=48 and ord(c) <=57)]

        if len(arr) <= 1:
            return True

        i = 0
        j = len(arr) - 1

        while i < j:
            if arr[i] != arr[j]:
                return False
            i += 1
            j -= 1
        return True

"""
Lower all
Remove non-alphanumeric chars
"""
