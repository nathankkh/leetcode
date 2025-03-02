class Solution:
    def punishmentNumber(self, n: int) -> int:
        '''
        Find the punishment number of n
        
        - The sum of squares of i such that 1 <= i <= n (i.e. all ints from 1 to n inclusive, which fulfil the next condition)
        - i is a number where i-squared can be grouped into substrings, such that the sum of the values can == i


        '''
        def check_partition(s: str, target: int, current_sum: int = 0) -> bool:
            # Base cases
            if not s:  # no more digits
                return current_sum == target
            
            # Try all possible partitions from current position
            for i in range(1, len(s) + 1):
                # Take current partition
                current_number = int(s[:i])
                
                # Skip if sum > target
                if current_sum + current_number > target:
                    continue
                    
                # Recursively check remaining string with updated sum
                if check_partition(s[i:], target, current_sum + current_number):
                    return True
            
            return False
        
        res = 0
        for i in range(n + 1):
            if check_partition(str(i*i), i):
                print(i)
                res += i*i

        return res
    
sol =Solution()
n = 10
out = 182
sol.punishmentNumber(n)