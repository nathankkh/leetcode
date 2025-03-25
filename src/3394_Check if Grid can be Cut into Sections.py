from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        """
        Given a list of rectangles, where each rectangle is represented by [start_x, start_y, end_x, end_y]
        Given a n * n grid

        return T/F if the grid can be split into 3 sections either vertically or horizontally
        -> there must be at least one rectangle in each section
        -> the split must not go through any rectangle

        rectangles are guaranteed not to overlap
        """

        def helper(arr):
            arr.sort()
            count = 0

            curr_end = arr[0][1]

            # keep checking if there is a gap between the most recent rectangle's ending coordinate and the next one's start
            for start, end in arr:
                if curr_end <= start:
                    count += 1

                curr_end = max(curr_end, end)

                if count == 2:
                    return True
            return False

        x_arr = [[r[0], r[2]] for r in rectangles]
        y_arr = [[r[1], r[3]] for r in rectangles]

        # check x
        return helper(x_arr) or helper(y_arr)


n = 5
rectangles = [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]
sol = Solution()
print("expected: true\n", "result: ", sol.checkValidCuts(n, rectangles))

n = 4
rectangles = [[0, 0, 1, 4], [1, 0, 2, 4], [2, 0, 3, 4], [3, 0, 4, 4]]
print("expected: true\n", "result: ", sol.checkValidCuts(n, rectangles))

n = 8
rectangles = [
    [0, 0, 3, 3],
    [0, 3, 1, 8],
    [1, 3, 2, 8],
    [2, 3, 3, 8],
    [3, 0, 5, 7],
    [5, 0, 6, 7],
    [6, 0, 7, 7],
    [7, 0, 8, 7],
    [3, 7, 8, 8],
]
print("expected: false\n", "result: ", sol.checkValidCuts(n, rectangles))
