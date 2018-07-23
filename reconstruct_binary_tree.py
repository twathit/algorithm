# -*- coding:utf-8 -*-
'''
重建二叉树
题目描述
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''

class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Solution(object):
	"""docstring for reconstruct_binary_tree"""
	def reconstruct_binary_tree(self, preorder,inorder):
		if len(preorder) == 0:
			return None
		if len(preorder) == 1:
			return TreeNode(preorder[0])
		else:
			root = TreeNode(preorder[0])
			root.left = self.reconstruct_binary_tree(preorder[1:inorder.index(preorder[0])+1],inorder[:inorder.index(preorder[0])])
			root.right = self.reconstruct_binary_tree(preorder[inorder.index(preorder[0])+1:],inorder[inorder.index(preorder[0])+1:])
		return root
		
if __name__ == '__main__':
	s=Solution()
	print(s.reconstruct_binary_tree([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6]))		