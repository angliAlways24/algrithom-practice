class TreeNode:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def BFSTree(root):
    if root is None:
        return
    
    queue = []
    queue.append(root)
    while len(queue) != 0:
        tmp = queue[0]
        queue = queue[1:]
        if tmp.left is not None:
            queue.append(tmp.left)
        if tmp.right is not None:
            queue.append(tmp.right)
        print(tmp.value)

def preOrder(root):
    if root is None:
        return
    
    print(root.value)
    preOrder(root.left)
    preOrder(root.right)
    
def inOrder(root):
    if root is None:
        return
    
    inOrder(root.left)
    print(root.value)
    inOrder(root.right)


def postOrder(root):
    if root is None:
        return
    
    postOrder(root.left)
    postOrder(root.right)
    print(root.value)



node = TreeNode(3)
node1 = TreeNode(1)
node.left = node1
node2 = TreeNode(7)
node.right = node2
node3 = TreeNode(6)
node1.left = node3
node4 = TreeNode(8)
node1.right = node4
node5 = TreeNode(9)
node2.left = node5
node6 = TreeNode(4) 
node2.right = node6
node7 = TreeNode(2)
node4.left = node7
node8 = TreeNode(5)
node5.right = node8

BFSTree(node)
print("-----------------")
preOrder(node)
print("-----------------")
inOrder(node)
print("-----------------")
postOrder(node)

