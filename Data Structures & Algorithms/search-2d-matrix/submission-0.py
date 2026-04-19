class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l , r = 0 , len(matrix) -1
        res = False

        while l <= r:
            m = matrix[(r+l) // 2]

            if target >= m[0] and target <= m[-1]:
                return target in m
            elif target < m[0] :
                r = matrix.index(m) - 1
            elif target > m[-1]:
                l = matrix.index(m) + 1
        return res 