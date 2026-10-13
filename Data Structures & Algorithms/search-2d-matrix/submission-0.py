class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        U, D = 0, len(matrix) - 1

        while U <= D:
            M = (U + D) // 2

            if matrix[M][0] > target: D = M - 1

            elif matrix[M][-1] < target: U = M + 1

            else:
                #binary search
                l = 0
                r = len(matrix[M]) - 1

                while l <= r:
                    m = (l + r) // 2

                    if matrix[M][m] < target: l = m + 1
                    elif matrix[M][m] > target: r = m - 1
                    else: 
                        return True

                return False

        return False