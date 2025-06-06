class Solution:
    def trap(self, height: list[int]) -> int:
        l,  n = 0, len(height)
        r = n-1

        # start with l & r on the outer edges
        # make the window shorter at each step while keeping track of where the 'walls' are
        # at each step, increment res by the (smaller of the walls  - current height)
        res = 0
        max_left, max_right = 0,0
        while r > l:
            if height[l] < height[r]:
                if height[l] > max_left: # begin a new 'pool' of trapped water
                    max_left = height[l]
                else: # this is part of a pool; there is a higher wall on left and right
                    res += max_left - height[l]
                l += 1

            else: # r >= l
                if height[r] > max_right:
                    max_right = height[r]
                else:
                    res += max_right - height[r]
                
                r -= 1
        return res

sol = Solution()
height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(sol.trap(height1))
print("expected: 6")


height2 = [4, 2, 0, 3, 2, 5]
print(sol.trap(height2))
print("expected: 9")

height3 = [4, 2, 3]
print(sol.trap(height3))
print("expected: 1")
