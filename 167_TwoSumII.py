class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int], 1-indexed
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1

        while True:
            curr = numbers[i] + numbers[j]
            if curr == target:
                break

            if curr < target: 
                i += 1
            else:
                j -= 1

        return [i+1,j+1]

''' 
Constraints:
- `numbers` is 1 indexed, in sorted increasing order
- Constant space must be used
- Exactly 1 answer exists
- No reusing elements 
- Could possibly have multiple elements of the same value

Brute force (n2)
for each element, iterate through all other elements

'''