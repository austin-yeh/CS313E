#  File: GraphFill.py
#  Description:
#  Student Name: Austin Yeh
#  Student UT EID: ay6922 
#  Partner Name: Eric Deng
#  Partner UT EID: cd36549
#  Course Name: CS 313E
#  Unique Number:
#  Date Created:
#  Date Last Modified:

import os
import sys
# this enables printing colors on Windows somehow
os.system("")

# code to reset the terminal color
RESET_CHAR = "\u001b[0m"
# color codes for the terminal
COLOR_DICT = {
	"black": "\u001b[30m",
	"red": "\u001b[31m",
	"green": "\u001b[32m",
	"yellow": "\u001b[33m",
	"blue": "\u001b[34m",
	"magenta": "\u001b[35m",
	"cyan": "\u001b[36m",
	"white": "\u001b[37m"
}
# character code for a block
BLOCK_CHAR = "\u2588"

# Input: text is some string we want to write in a specific color
#   color is the name of a color that is looked up in COLOR_DICT
# Output: returns the string wrapped with the color code
def colored(text, color):
	color = color.strip().lower()
	if not color in COLOR_DICT:
		raise Exception(color + " is not a valid color!")
	return COLOR_DICT[color] + text

# Input: color is the name of a color that is looked up in COLOR_DICT
# prints a block (two characters) in the specified color
def print_block(color):
	print(colored(BLOCK_CHAR, color)*2, end='')

# Stack class; you can use this for your search algorithms
class Stack(object):
	def __init__(self):
		self.stack = []

	# add an item to the top of the stack
	def push(self, item):
		self.stack.append(item)

  	# remove an item from the top of the stack
	def pop(self):
		return self.stack.pop()

  	# check the item on the top of the stack
	def peek(self):
		return self.stack[-1]

  	# check if the stack if empty
	def is_empty(self):
		return len(self.stack) == 0

  	# return the number of elements in the stack
	def size(self):
		return len(self.stack)

# Queue class; you can use this for your search algorithms
class Queue(object):
	def __init__(self):
		self.queue = []

  	# add an item to the end of the queue
	def enqueue(self, item):
		self.queue.append(item)

  	# remove an item from the beginning of the queue
	def dequeue(self):
		return self.queue.pop(0)

  	# checks the item at the top of the Queue
	def peek(self):
		return self.queue[0]

  	# check if the queue is empty
	def is_empty(self):
		return len(self.queue) == 0

  	# return the size of the queue
	def size(self):
		return len(self.queue)

# class for a graph node; contains x and y coordinates, a color, a list of edges and
# a flag signaling if the node has been visited (useful for serach algorithms)
# it also contains a "previous color" attribute. This might be useful for your flood fill implementation.
class ColorNode:
	# Input: x, y are the location of this pixel in the image
	#   color is the name of a color
	def __init__(self, x, y, color):
		self.color = color
		self.prev_color = color
		self.x = x
		self.y = y
		self.edges = []
		self.visited = False

	# Input: node_index is the index of the node we want to create an edge to in the node list
	# adds an edge and sorts the list of edges
	def add_edge(self, node_index):
		self.edges.append(node_index)
		self.edges.sort()

	# Input: color is the name of the color the node should be colored in;
	# the function also saves the previous color (might be useful for your flood fill implementation)
	def set_color(self, color):
		self.prev_color = self.color
		self.color = color

# class that contains the graph
class ImageGraph:
	def __init__(self, image_size):
		self.nodes = []
		self.image_size = image_size

	# prints the image formed by the nodes on the command line
	def print_image(self):
		img = [["black" for i in range(self.image_size)] for j in range(self.image_size)]

		# fill img array
		for node in self.nodes:
			img[node.y][node.x] = node.color

		for line in img:
			for pixel in line:
				print_block(pixel)
			print()
		# print new line/reset color
		print(RESET_CHAR)

	# sets the visited flag to False for all nodes
	def reset_visited(self):
		for i in range(len(self.nodes)):
			self.nodes[i].visited = False

	# implement your adjacency matrix printing here.
	def print_adjacency_matrix(self):
		print("Adjacency matrix:")

		lsts = [[1 if j in self.nodes[i].edges else 0 for j in range(len(self.nodes))] for i in range(len(self.nodes))]

		
		for lst in lsts:
			for el in lst:
				print(el, end="")
			print()
		
		# empty line afterwards
		print()

	# implement your bfs algorithm here. Call print_image() after coloring a node
	# Input: graph is the graph containing the nodes
	#   start_index is the index of the currently visited node
	#   color is the color to fill the area containing the current node with
	def bfs(self, start_index, color):
		# reset visited status
		self.reset_visited()
		# print initial state
		print("Starting BFS; initial state:")
		self.print_image()

		# raise NotImplementedError("Remove this exception and implement the bfs algorithm here.")
		q = Queue()
		q.enqueue(self.nodes[start_index])
		original_color = self.nodes[start_index].color
		while not q.is_empty():
			for _ in range(q.size()):
				node = q.dequeue()
				if node.color == original_color:
					node.visited = True
					node.set_color(color)
					self.print_image()
					for i in node.edges:
						if not self.nodes[i].visited:
							q.enqueue(self.nodes[i])

	# implement your dfs algorithm here. Call print_image() after coloring a node
	# Input: graph is the graph containing the nodes
	#   start_index is the index of the currently visited node
	#   color is the color to fill the area containing the current node with
	def dfs(self, start_index, color):
		# reset visited status
		self.reset_visited()
		# print initial state
		print("Starting DFS; initial state:")
		self.print_image()

		# raise NotImplementedError("Remove this exception and implement the dfs algorithm here.")
		s = Stack()
		s.push(self.nodes[start_index])
		original_color = self.nodes[start_index].color
		self.nodes[start_index].visited = True
		self.nodes[start_index].set_color(color)
		self.print_image()
		while not s.is_empty():
			current = s.peek()
			for i in current.edges:
				if self.nodes[i].color == original_color:
					self.nodes[i].visited = True
					self.nodes[i].set_color(color)
					self.print_image()
					s.push(self.nodes[i])
					break
			else:
				s.pop()

def main():
	dimension = int(sys.stdin.readline())
	graph = ImageGraph(dimension)

	for _ in range(int(sys.stdin.readline())):
		line = sys.stdin.readline().strip().split(',')
		cnode = ColorNode(int(line[0]), int(line[1]), line[2])
		graph.nodes.append(cnode)

	for _ in range(int(sys.stdin.readline())):
		line = sys.stdin.readline().strip().split(',')
		graph.nodes[int(line[0])].add_edge(int(line[1]))
		graph.nodes[int(line[1])].add_edge(int(line[0]))

	# print matrix
	graph.print_adjacency_matrix()

	bfs_line, dfs_line = sys.stdin.readline().strip().split(','), sys.stdin.readline().strip().split(',')
	bfs_start, bfs_color, dfs_start, dfs_color = int(bfs_line[0]), bfs_line[1], int(dfs_line[0]), dfs_line[1]

	# # run bfs
	graph.bfs(bfs_start, bfs_color)

	# # run dfs
	graph.dfs(dfs_start, dfs_color)


if __name__ == "__main__":
	main()
