# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(preorder[0])
        stack = [root]
        for i in preorder[1:]:
            i = TreeNode(i)
            if i.val<stack[-1].val:
                stack[-1].left = i
                stack.append(i)
            else:
                while stack and stack[-1].val<i.val:
                    last = stack.pop(-1)
                last.right = i
                stack.append(i)
        return root
