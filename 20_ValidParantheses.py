class Solution:
    def isValid(self, s: str) -> bool:
        parantheses = {")": "(", "}": "{", "]": "["}  # closing
        stack = []
        if len(s) % 2 != 0:
            return False
        for char in s:
            if char in parantheses:
                if not stack or stack.pop() != parantheses[char]:
                    return False
            else:
                stack.append(char)
        return not stack
