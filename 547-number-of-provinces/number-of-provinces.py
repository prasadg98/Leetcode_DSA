class Solution:

    def dfs(self, i, isConnected, visited):
        visited[i] = True
        for x in range(len(isConnected[i])):
            if isConnected[i][x] == 1 and visited[x] == False:
                self.dfs(x, isConnected, visited)


    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        total_provinces = 0

        for i in range(n):
            if not visited[i]:
                self.dfs(i, isConnected, visited)
                total_provinces += 1

        return total_provinces