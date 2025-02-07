# Given an integer array nums and an integer k, 
# return the k most frequent elements. 
# You may return the answer in any order.


class Solution:
    def topKFrequent(self, num, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        freq = [[] for i in range(len(num)+1) ]

        for i in num:
            if i in count:
                freq[count[i]].remove(i)
                count[i] += 1
            else:
                count[i] = 1

            freq[count[i]].append(i)
        
        res = []
        for i in range(len(freq) - 1, 0, -1): # iterate backward
            if freq[i]:
                for num in freq[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
                    
    def topKFrequent(self, num, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        for i in num:
            if i in count:
                count[i] += 1
            else:
                count[i] = 0
        
        temp = sorted(list(count.items()), key= lambda x: x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(temp[i][1])

        return res