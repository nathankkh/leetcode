import heapq
from collections import defaultdict

class NumberContainers(object):
    # Store / Replace at index
    # Given a number, find the smallest index if exists

    '''    
        to_find:
            {
                number1: [idx1, idx2],
                number2: [idx3, idx4]
            }
    '''

    def __init__(self):
        self.index_to_num = {}
        self.num_to_index = defaultdict(list)
        self.to_remove = defaultdict(set) # for lazy deletion
        

    def change(self, index, number):
        """
        :type index: int
        :type number: int
        :rtype: None
        """
        if index in self.index_to_num: # index has been added to, change it        
            # retrieve the number and pop it from self.to_find
            old_num = self.index_to_num[index]
            self.to_remove[old_num].add(index)

        # update list
        self.index_to_num[index] = number
        # update helper
        heapq.heappush(self.num_to_index[number], index)
        
    def find(self, number):
        """
        :type number: int
        :rtype: int
        """
        if number not in self.num_to_index:
            return -1
        idx_heap = self.num_to_index[number]

        while idx_heap:
            curr = idx_heap[0] # idx 

            # if it maps to target number, return
            if self.index_to_num[curr] == number:
                return curr
            else:
                heapq.heappop(idx_heap)
        return -1