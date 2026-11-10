class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N, M = len(matrix), len(matrix[0])
        left = 0
        right = M * N - 1

        while left <= right:
            mid = (left + right) // 2
            i, j = mid // M, mid % M

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
