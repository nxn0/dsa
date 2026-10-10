# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        ans=[]
        q=deque([root])
        while q:
            xl = float('-inf')
            for _ in range(len(q)):
                node = q.popleft()
                xl = max(xl,node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(xl)
        return ans
            
        