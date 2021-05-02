class Node:
	def __init__(self, data = None, next_node = None):
		self.data = data
		self.next = next_node

class LinkedList:
	def __init__(self):
		self.head = None


	def insert_at_head(self, data):
		if self.head == None:
			self.head = Node(data)
			return

		new_head = Node(data, self.head)
		self.head = new_head

	def insert_after(self, prev_data, new_data):
		new_node = Node(new_data)

		node = self.head
		while(node):
			if node.data == prev_data:
				new_node.next = node.next
				node.next = new_node

			node = node.next


	def insert_at_tail(self, new_data):

		new_node = Node(new_data)

		if self.head is None:
			self.head = new_node
			return

		node = self.head
		while(node.next != None):
			node = node.next

		node.next = new_node

	def delete_at_head(self):
		if self.head is None:
			print("LinkedList already empty!")
			return

		self.head = self.head.next

	def delete_key(self, data):
		if self.head is None:
			print("LinkedList already empty!")
			return

		if self.head.data == data:
			return self.delete_at_head()
		
		curr = self.head
		prev = None

		while curr:
			if curr.data == data:
				break

			prev = curr
			curr = curr.next

		if curr == None:
			return

		prev.next = curr.next

	def delete_at_position(self,position):
		"""Position starts at zero and it deletes the node at the position"""
		if self.head is None:
			print("LinkedList already empty!")
			return

		if position == 0:
			return self.delete_at_head()
		
		curr = self.head

		for _ in range(position-1):
			curr = curr.next
			if curr is None:
				break

		if curr is None:
			print("Invalid position")
			return
		if curr.next is None:
			print("Invalid position")
			return

		temp = curr.next.next
		curr.next = None
		curr.next = temp

	def delete_at_tail(self):
		if self.head is None:
			print("LinkedList already empty!")
			return

		node = self.head
		while node.next.next:
			node = node.next

		node.next = None

	def print_ll(self):

		node = self.head
		
		if node is None:
			print("LinkedList is empty")
			return

		print("LinkedList: ", end="")
		while node:
			print(f"{node.data} -> ", end="")
			node = node.next

		print("NULL")

'''
if __name__ == "__main__":
	
	ll = LinkedList()
	ll.insert_at_head(3)
	ll.print_ll()
	print()
	ll.insert_at_tail(15)
	ll.print_ll()
	print()
	ll.insert_after(3,5)
	ll.print_ll()
	print()
	ll.insert_after(5,7)
	ll.print_ll()
	print()
	ll.delete_at_position(2)
	ll.print_ll()
	print()
	ll.delete_at_head()
	ll.print_ll()
	print()
	ll.delete_at_tail()
	ll.print_ll()
	print()
	ll.delete_key(5)
	ll.print_ll()
	print()
	#print(ll.head.data)
'''