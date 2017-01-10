 
class Node(object):
 	def __init__(self, data, dad):
 		self.data = data
 		self.children = []
 		self.dad = dad

 	def add_child(self, obj):
 		self.children.append(obj)

 	def get_child(self):
 		return self.children

 	def get_dad(self):
 		return self.dad

 	def get_data(self):
 		return self.data

 	def remove_child(self, node):
 		try:
 			self.children.remove(node)
 		except:
 			print(self.data)
 		
 	def remove_child_lm(self, node):
 		self.children.remove(node)
 		if len(self.children) == 0:
 			dad.remove_child(node)
 	def print_data(self):
 		print(self.data)