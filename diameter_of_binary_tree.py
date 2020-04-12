# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def findDepth(root):

    if root is None:
        return 0

    return 1 + max(findDepth(root.left), findDepth(root.right))

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        left = findDepth(root.left)
        right = findDepth(root.right)

        ldia = self.diameterOfBinaryTree(root.left)
        rdia = self.diameterOfBinaryTree(root.right)


        return max(left+right, max(ldia, rdia))
