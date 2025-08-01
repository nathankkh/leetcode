class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            prev = res[-1]
            curr = [1]
            # current row number: number of elements in the previous row
            for j in range(1, i):
                curr.append(prev[j-1]+prev[j])
            curr.append(1)
            res.append(curr)
        return res