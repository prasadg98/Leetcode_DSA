class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0,1,2
        m,n = len(grid), len(grid[0])
        fresh_oranges = 0
        q = collections.deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == ROTTEN:
                    q.append((i,j))
                elif grid[i][j] == FRESH:
                    fresh_oranges += 1
        
        if fresh_oranges == 0:
            return 0

        min_minutes = -1
        while q:
            size = len(q)
            min_minutes +=1
            for _ in range(size):
                i,j = q.popleft()
                for r,c in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == FRESH:
                        grid[r][c] = ROTTEN
                        q.append((r,c))
                        fresh_oranges -= 1

        if fresh_oranges == 0:
            return min_minutes
        else:
            return -1
                    

         