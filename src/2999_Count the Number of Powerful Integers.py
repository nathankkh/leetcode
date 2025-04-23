from collections import deque

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        if int(s) > finish:
            return 0
        n = len(str(finish))
        # initialise the starting value 
        arr = deque([_ for _ in s])
        if int(s) < start: 
            diff_in_digits = len(str(start)) - len(s)
            temp_num = str(start)[0]
            for _ in range(diff_in_digits):
                arr.appendleft(min(temp_num, limit))

        count = 1
        running_val = int(s)
        power = 1
        while True:
            if len(arr) < n:
                count += limit ** power
                arr.appendleft(str(limit))
                power += 1
                continue
            else:
                # final pass
                running_val = int(''.join(arr))
                final_counter = 0
                while running_val < finish:
                    final_counter += 1
                    
                    new_prefix = int(arr[0]) + 1
                    if new_prefix > limit or new_prefix == 10:
                        break
                    else:
                        arr[0] = str(new_prefix)
                        running_val = int(''.join(arr))
                count += final_counter ** power
                break
        return count
            
