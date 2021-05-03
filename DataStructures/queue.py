### Using list

class Node:
	def __init__(self, data = None, next_node = None):
		self.data = data
		self.next = next_node

class Queue:
	"""docstring for Queue using list in python"""
	def __init__(self):
		self.queue = []

	def Enqueue(self, data):
		self.queue.append(data)

	def isEmpty(self):
		return len(self.queue) < 1

	def Dequeue(self):
		if self.isEmpty():
			return None

		return self.queue.pop(0)

	def size(self):
		return len(self.queue)
	
	def display(self):
		print(self.queue)

'''
if __name__ == "__main__":
	q = Queue()
	q.Enqueue(2)
	q.Enqueue(4)
	q.Enqueue(1)
	q.display()
	q.Dequeue()
	q.display()
'''