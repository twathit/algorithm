'''
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''

class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, x):
		self.x = x
		self.left = None
		self.right = None
		self.parent = None

class Solution(object):
	"""docstring for Solution"""
	def get_next(self,pNode):
		if pNode is None:
			return None
		if pNode.right:
			pRight = pNode.right
			while pRight.left:
				pRight = pRight.left
			pNext = pRight
		elif pNode.parent:
			pParent = pNode.pParent
			while pParent and pNode == pParent.right:
				pNode = pParent
				pParent = pParent.parent
			pNext = pParent
		return pNext
		
		