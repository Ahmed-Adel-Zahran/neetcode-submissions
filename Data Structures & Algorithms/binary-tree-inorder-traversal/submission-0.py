# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative solution
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        curr = root
        while stack or curr:
            # go all the way to the left most leaf node
            while curr:
                # append all the left nodes to the stack 
                stack.append(curr)
                curr = curr.left
            # pop that left most leaf node and point to it 
            curr = stack.pop()
            # add it to the result 
            res.append(curr.val)
            # move to the right node and repeat 
            curr = curr.right
        return res  



        