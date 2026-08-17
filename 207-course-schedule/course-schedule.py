import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        q = collections.deque()
        Inorder = [0] * n
        ans = []

        adjList = []

        for i in range(n):
            adjList.append([])

        for course, pre in prerequisites:
            adjList[pre].append(course)
            Inorder[course] += 1

        for i in range(n):
            if Inorder[i] == 0:
                ans.append(i)
                q.append(i)

        while q:
            front = q.popleft()
            for x in adjList[front]:
                Inorder[x] -= 1
                if Inorder[x] == 0:
                    q.append(x)
                    ans.append(x)

        if len(ans) == n:
            return True
        else:
            return False



        


