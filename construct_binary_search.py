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
        if len(preorder)==0: return None
        
        root = TreeNode(preorder[0])
        
        ind=1
        while ind<len(preorder) and preorder[ind]<preorder[0]: ind+=1
            
        root.left = self.bstFromPreorder(preorder[1:ind])
        root.right= self.bstFromPreorder(preorder[ind:])
        
        return root
