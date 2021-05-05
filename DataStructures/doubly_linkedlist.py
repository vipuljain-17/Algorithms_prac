class Node:
	def __init__(self, data = None, prev_node = None, next_node = None):
		"""
		Internal node class to represent data
		data = value
		next = pointer to next node
		prev = pointer to prev node
		"""
		self.data = data
		self.prev = prev_node
		self.next = next_node

	def __repr__(self):
		return f"{self.data}"

class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.llsize = 0

	def __len__(self):
		return self.llsize

	def size(self):
		return self.llsize

	def isEmpty(self):
		return self.size() < 1

	def insert_at_head(self, data):
		if self.isEmpty():
			self.head = self.tail = Node(data)
			
		else:
			self.head.prev= Node(data, None, self.head)
			self.head = self.head.prev

		self.llsize += 1

	def insert_at_tail(self,data):
		if self.isEmpty():
			self.head = self.tail = Node(data)

		else:
			self.tail.next = Node(data, self.tail, None)
			self.tail = self.tail.next

		self.llsize += 1

	def insertAt(self, data, pos):
		if pos < 0:
			raise Exception("index should not be negative!")

		if pos == 0:
			return self.insert_at_head(data)

		if pos == self.llsize:
			return self.insert_at_tail(data)

		temp = self.head
		for i in range(pos-1):
			temp = temp.next

		newNode = Node(data, temp, temp.next)
		temp.next.prev = newNode
		temp.next = newNode

		self.llsize += 1

	def peekFirst(self):
		if self.isEmpty():
			raise Exception("List already Empty!")

		return self.head.data

	def peekLast(self):
		if self.isEmpty():
			raise Exception("List already Empty!")

		return self.tail.data

	def delete_at_head(self):
		if self.isEmpty():
			raise Exception("List already Empty!")

		data = self.head.data
		self.head = self.head.next
		self.llsize -= 1

		if self.isEmpty():
			self.tail = None

		else:
			self.head.prev = None

		return data

	def delete_at_tail(self):
		if self.isEmpty():
			raise Exception("List already Empty!")

		data = self.tail.data
		self.tail = self.tail.prev
		self.llsize -= 1

		if self.isEmpty():
			self.head = None

		else:
			self.tail.next = None

	def delete_key(self, key):
		if key == None:
			return None

		if self.isEmpty():
			raise Exception("List already Empty!")

		if self.head.data == key:
			return self.delete_at_head()

		curr = self.head
		while curr:
			if curr.data == key:
				self.llsize -= 1
				curr.prev.next = curr.next
				curr.next.prev = curr.prev
				return

		if curr is None:
			print("Key missing!")
			return

	def __remove__(self, node):
		if node.prev == None:
			return self.delete_at_head()
		if node.next == None:
			return self.delete_at_tail()

		data = node.data
		node.prev.next = node.next
		node.next.prev = node.prev

		self.llsize -= 1

		return data


	def deleteAt(self, pos):
		if pos < 0 or pos >= self.llsize:
			raise ValueError("Wrong index!")

		if pos < self.llsize / 2:
			i = 0
			trav = self.head
			while i != pos:
				i += 1
				trav = trav.next

		else:
			i = self.llsize - 1
			trav = self.tail

			while i != pos:
				i -= 1
				trav = trav.prev


		return self.__remove__(trav)

	def print_ll(self):
		curr = self.head

		if curr is None:
			print("LinkedList is empty")
			return

		print("LinkedList: ", end="")
		while curr:
			print(f"{curr.data} -> ", end="")
			curr = curr.next

		print("NULL")

	def print_ll_reverse(self):
		curr = self.tail

		if curr is None:
			print("LinkedList is empty")
			return

		print("Reverse LinkedList: ", end="")
		print("NULL", end="")
		while curr:
			print(f" <- {curr.data}", end="")
			curr = curr.prev
		print()

"""
if __name__ == "__main__":
	ll = DoublyLinkedList()
	ll.insert_at_head(3)
	ll.print_ll()
	print()
	ll.insert_at_head(5)
	ll.print_ll()
	print()
	ll.insert_at_tail(100)
	ll.print_ll_reverse()
	print()
	ll.delete_at_head()
	ll.print_ll()
	print()
	ll.insertAt(95,1)
	ll.print_ll()
	print()
	ll.delete_at_tail()
	ll.print_ll()
	print()
	ll.deleteAt(1)
	ll.print_ll()
	print()
	ll.delete_key(3)
	ll.print_ll()
	print()
	ll.insert_at_head(99)
	ll.print_ll()
	print()
"""