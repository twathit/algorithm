#Print a singly linked list from tail to head.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	#运用栈“后进先出”
	def printLinkedList1(self,head):
		stack=[]
		while head:
			stack.append(head.val)
			head=head.next
		while stack:
			print(stack[-1])
			stack.pop()
	#递归调用
	def printLinkedList2(self,head):
		if head:
			if head.next:
				self.printLinkedList2(head.next)
			print(head.val)
		

if __name__=='__main__':
	head=ListNode(1)  
	p1=ListNode(4)  
	p2=ListNode(3)  
	p3=ListNode(5)  
	head.next=p1  
	p1.next=p2  
	p2.next=p3
	s=Solution()
	s.printLinkedList1(head)
	s.printLinkedList2(head)
