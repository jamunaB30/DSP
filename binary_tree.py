class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def create(root):
    data=int(input("Enter the data"))
    new_root=Node(data)
    root=insert(root,new_root)
    return root
def insert(root,new_root):
    if(root==None):
        root=new_root
    else:
        if(new_root.data<=root.data):
            root.left=insert(root.left,new_root)
        else:
            root.right=insert(root.right,new_root)
    return root
def inorder(root):
    if(root==None):
        return[]
    else:
        result=[]
        result.extend(inorder(root.left))
        result.append(root.data)
        result.extend(inorder(root.right))
        return result
def postorder(root):
    if(root==None):
        return[]
    else:
        result=[]
        result.extend(inorder(root.left))
        result.extend(inorder(root.right))
        result.append(root.data)
        return result
def preorder(root):
    if(root==None):
        return[]
    else:
        result=[]
        result.append(root.data)
        result.extend(inorder(root.left))
        result.extend(inorder(root.right))
        return result
root=None
for i in range(0,5):
    root=create(root)
print(inorder(root))
print(preorder(root))
print(postorder(root))
