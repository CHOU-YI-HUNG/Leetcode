# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        self.toAdd = 0
        self.hash = {}
        for idx in range(len(inorder)):
            self.hash[inorder[idx]] = idx
        return self.rec(0, len(inorder) - 1, preorder, inorder)

    def rec(self, left, right, preorder, inorder):
        if left > right or self.toAdd >= len(inorder):
            return None
        node = TreeNode(preorder[self.toAdd])
        self.toAdd += 1
        """ if left == right:
            return node """
        node.left = self.rec(left, self.hash[node.val] - 1, preorder, inorder)
        node.right = self.rec(self.hash[node.val] + 1, right, preorder, inorder)
        return node
        