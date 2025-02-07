class Solution(object):
    # N^2 answer
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        arr = [c for c in boxes]
        res = []
        for i in range(len(boxes)):
            curr = 0
            for j in range(len(boxes)):
                if arr[j] == '1':
                    curr += abs(i-j)
            res.append(curr)
        return res
    
    # O(N)
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        arr = [c for c in boxes] # array of chars
        res = []
        