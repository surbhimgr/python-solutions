class Tree:
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None
def modifytree(root):
    if root==None:
        return
    nodestack=[]
    pre=None
    nodestack.append(root)
    while(len(nodestack)):
        node=nodestack[-1]
        nodestack.pop()
        if node.right:
            nodestack.append(node.right)
        if node.left:
            nodestack.append(node.left)
        if pre:
            pre.right=node
        pre=node
def printtree(root):
    node=root
    while(node):
        print(node.val,end=" ")
        node=node.right
root=Tree(10)
root.left=Tree(8)
root.right=Tree(2)
root.right.left=Tree(3)
root.right.right=Tree(5)
modifytree(root)
printtree(root)
        
