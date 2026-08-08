# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = deque()
        queue.append(root)

        if not root:
            return []

        while queue:
            n = len(queue)
            maxL = queue[0].val
            for i in range(n):
                node = queue.popleft()
                maxL = max(maxL, node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            result.append(maxL)

        return result
            


        

        