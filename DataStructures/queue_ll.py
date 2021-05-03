## Using Linked List

class Node:
	def __init__(self, data = None, next_node = None):
		self.data = data
		self.next = next_node

class Queue:
	"""docstring for Queue using linked list in python"""
	def __init__(self):
		self.head = None
		self.tail = None
	
	def EnQueue(self, data):
		if self.tail is None and self.head is None:
			self.tail = self.head = Node(data)
			return

		self.tail.next = Node(data)
		self.tail = self.tail.next

	def isEmpty(self):
		return self.head == None

	def DeQueue(self):
		if self.isEmpty():
			return None

		temp = self.head
		
		self.head = self.head.next
		
		if self.head is None:
			self.tail = None
		
		return temp

	def __str__(self):
		if self.isEmpty():
			return None

		print("Queue - ", end="")
		out = ""
		curr = self.head
		while curr:
			out += str(curr.data) + "->"
			curr = curr.next

		return out[:-2]
'''
if __name__== '__main__':
	q = Queue()
	q.EnQueue(10)
	q.EnQueue(20)
	print(q)
	q.DeQueue()
	print(q)
	q.DeQueue()
	q.EnQueue(30)
	q.EnQueue(40)
	q.EnQueue(50)
	q.DeQueue()

	print(q)
 '''
 