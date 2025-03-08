from typing import List
class Solution:
    def countBadPairs(self, nums:List[int]) -> int:
        # nums(j) - nums(i) != j - i
        # nums(j) - j = nums(i) - i
        # as the counter increases, nums[counter] could have made pairs with all previous elements
        # take nums(i) - i and compare with the hashmap. map.get((nums[i]-i)) will return the number of previous elements that would form a good pair with the current element
        # Since all previous elements are potential pairs, take (prev_elem_count - good_pairs_count) to get number of bad elements
        n = len(nums)
        good_pairs=0
        pair_count = {} # stores nums[i]-i {diff: count}
        for i in range (n): 
            curr_diff = nums[i] - i
            # see if any previous elements match the current diff
            num_good_pair = pair_count.get(curr_diff, 0)
            good_pairs += num_good_pair
            pair_count[curr_diff] = num_good_pair + 1
        
        total_pairs = (n * (n - 1)) // 2
        return total_pairs - good_pairs