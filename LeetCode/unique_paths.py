class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo = [[0] * m for _ in range(n)]

        # 10 6 3 1
        # 4 3 2 1
        # 1 1 0 1
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if i == n-1 and j == m - 1:
                    memo[i][j] = 1
                elif i == n-1:
                    memo[i][j] = memo[i][j+1]
                elif j == m-1:
                    memo[i][j] = memo[i+1][j]
                else:
                    memo[i][j] = memo[i+1][j] + memo[i][j+1]
        
        return memo[0][0]
        
