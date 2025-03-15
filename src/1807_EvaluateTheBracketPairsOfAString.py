from typing import List
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d={}
        n = len(knowledge[0])
        for i in range(n):
            d[knowledge[0][i]] = knowledge[1][i]
        
        temp = []
        left = 0
        res = ''
        while True:
            idx = s.find('(')
            if idx == -1:
                res+=s[left+1:]
            else:
                pass