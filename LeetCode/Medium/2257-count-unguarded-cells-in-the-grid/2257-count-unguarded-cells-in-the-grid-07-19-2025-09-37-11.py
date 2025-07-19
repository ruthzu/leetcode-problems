class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        grid = [[0]*n for i in range(m)]
        for r,c in walls:
            grid[r][c]='w'
        for r,c in guards:
            grid[r][c]='g'
        dir=[(-1,0),(1,0),(0,-1),(0,1)]
        for r,c in guards:
            for dr,dc in dir:
                nr=dr+r
                nc=dc+c
                while 0<=nr<m and 0<=nc<n:
                    if grid[nr][nc] in ('w','g'):
                        break
                    if grid[nr][nc]==0:
                        grid[nr][nc]='x'
                    nr+=dr
                    nc+=dc        

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1

        return count    
