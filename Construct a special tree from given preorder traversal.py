#Amazon wow
class Tree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
pre=[10,30,20,5,15]
preLN=['N','N','L','L','L']
n=len(pre)
i=[0]
root=Tree(pre[0])
def treemaker(node):
    if i[0]==n:
        return
    if preLN[i[0]]=='L':
        return Tree(pre[i[0]])
    if preLN[i[0]]=='N':
        i[0]+=1
        temp=Tree(pre[i[0]])
        node.left=treemaker(temp)
        i[0]+=1
        temp=Tree(pre[i[0]])
        node.right=treemaker(temp)
        if(i[0]>0):
            return node
def printInorder (node):
    if node == None:
        return
    printInorder (node.left)
    print(node.val,end=" ")
    printInorder (node.right)
treemaker(root)
printInorder(root)
        
        
    
