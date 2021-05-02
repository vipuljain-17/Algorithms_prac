### Using Linked List

class Node:
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

class Stack:
	def __init__(self):
		self.head = None
		self.size = 0

	def __str__(self):
		if self.isEmpty():
			return None
		print("Stack - ", end="")
		out = ""
		curr = self.head
		while curr:
			out += str(curr.data) + "->"
			curr = curr.next

		return out[:-2]

	def getSize(self):
		return self.size

	def isEmpty(self):
		return self.size == 0

	def peek(self):
		if self.isEmpty():
			print("Stack is Empty!")
			return

		return self.head.data

	def push(self, val):
		node = Node(val)

		if self.isEmpty():
			self.head = node
			self.size += 1
			return

		node.next = self.head
		self.head = node
		self.size += 1

	def pop(self):
		if self.isEmpty():
			print("Stack is Empty!")
			return

		self.head = self.head.next
		self.size -= 1

'''
if __name__ == "__main__":
	stack = Stack()
	for i in range(1, 11):
		stack.push(i)

	print(stack)

	for _ in range(1, 6):
		stack.pop()

	print(stack)

	stack.pop()
	print(stack.peek())
'''