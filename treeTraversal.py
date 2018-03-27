class Node:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.val = value
	
def preorder(root):
	if isinstance(root, Node):
		print(root.val),
		preorder(root.left)
		preorder(root.right)
		
def postorder(root):
	if isinstance(root, Node):
		preorder(root.left)
		preorder(root.right)
		print(root.val)
		
def inoderorder(root):
	if isinstance(root, Node):
		preorder(root.left)
		print(root.val)
		preorder(root.right)
		
		
		
root = Node(1)
root.left      = Node(2)
root.right     = Node(3)
root.left.left  = Node(4)
root.left.right  = Node(5)
print( "Preorder traversal of binary tree is")
preorder(root)
print( "Postorder traversal of binary tree is")
postorder(root)
print( "Inoder traversal of binary tree is")
inoderorder(root)
