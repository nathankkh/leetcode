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

        # removal
        while idx_heap and idx_heap[0] in self.to_remove[number]:
            heapq.heappop(idx_heap)
        
        return idx_heap[0] if idx_heap else -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)

instructions=["find","change","change","change","change","find","change","find"]
nums = [[10],[2,10],[1,10],[3,10],[5,10],[10],[1,20],[10]]
obj = NumberContainers()

count = 0
res = []
for i in instructions:
    match(i):
        case "find":
            
            res.append(obj.find(nums[count][0]))
        case "change":
            obj.change(nums[count][0], nums[count][1])
            res.append('null')
    count += 1

print(res)

instructions=["change","find","change","find","find","find"]
nums = [[1,10],[10],[1,20],[10],[20],[30]]
obj = NumberContainers()

count = 0
res = []
for i in instructions:
    match(i):
        case "find":
            
            res.append(obj.find(nums[count][0]))
        case "change":
            obj.change(nums[count][0], nums[count][1])
            res.append('null')
    count += 1

print(res)

