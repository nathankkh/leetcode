class Solution:
    def countSegments(self, s: str) -> int:
        s=s.strip()
        if s == '':
            return 0
        return len(s.split())