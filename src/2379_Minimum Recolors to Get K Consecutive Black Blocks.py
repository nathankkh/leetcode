class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left,right = 0,k-1
        res = curr = sum([1 for x in range(k) if blocks[x] == 'W'])
        
        while right < len(blocks)-1:
            if blocks[left] == 'W':
                curr -= 1
            if blocks[right+1] == 'W':
                curr +=1
            res = min(res,curr)
            left +=1
            right +=1
        return res