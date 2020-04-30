# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidSequence(self, root, arr):
        """
        :type root: TreeNode
        :type arr: List[int]
        :rtype: bool
        """
        if (root==None): return len(arr)==0
        return self.isvalid(root,arr,0)
    
    def isvalid(self,root,arr,idx):
        if (root.val!=arr[idx]): return False
        if (idx ==len(arr)-1): 
            return root.left == None and root.right == None
        return ((root.left!=None and self.isvalid(root.left,arr,idx+1)) or (root.right!=None and self.isvalid(root.right,arr,idx+1)))
