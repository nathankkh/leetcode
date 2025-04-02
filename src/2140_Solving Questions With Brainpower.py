from typing import List


class Solution:
    # no DP
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)

        def helper(idx, curr_points):
            if idx >= n:
                return curr_points
            else:
                points, brainpower = questions[idx]
                if idx == n - 1:
                    return points + curr_points

                return max(
                    # else take
                    helper(idx + brainpower + 1, curr_points + points),
                    helper(idx + 1, curr_points),
                )

        return helper(0, 0)

    # dp - recursive
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        d = [-1 for _ in range(n)]

        def helper(idx):
            if idx >= n:
                return 0
            elif d[idx] != -1:
                return d[idx]
            else:
                points, brainpower = questions[idx]

                take = points + helper(idx + brainpower + 1)
                skip = helper(idx + 1)
                d[idx] = max(take, skip)
                return d[idx]

        return helper(0)

    # dp - iterative
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        d = [0 for _ in range(n + 2)]

        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            take = points + (d[i + brainpower + 1] if (i + brainpower + 1) < n else 0)
            skip = d[i + 1]
            d[i] = max(take, skip)
        return d[0]
