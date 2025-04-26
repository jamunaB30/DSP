import time
class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def create(root):
    data=int(input("Enter the data"))
    new_root=Node(data)
    root=insert(root,new_root)
    return root
def insert(root,new_root):
    if root==None:
        root=new_root
    else:
        if new_root.data<=root.data:
            root.left=insert(root.left,new_root)
        else:
            root.right=insert(root.right,new_root)
    return root

def inorder(root):
    if root==None:
        return []
    else:
        result=[]
        result.extend(inorder(root.left))
        result.append(root.data)
        result.extend(inorder(root.right))
        return result
def preorder(root):
    if root==None:
        return []
    else:
        result=[]
        result.append(root.data)
        result.extend(inorder(root.left))
        result.extend(inorder(root.right))
        return result
def postorder(root):
    if root==None:
        return []
    else:
        result=[]
        result.extend(inorder(root.left))
        result.extend(inorder(root.right))
        result.append(root.data)
        return result
root=None
n=int(input("Enter the number of elements:"))
for i in range(n):
    root=create(root)
print(root)

while True:
    print("Menu")
    print("1.inorder")
    print("2.preorder")
    print("3.postorder")
    print("4.exit")

    opt=int(input("Enter the your option"))

    if opt==1:
        start=time.time()
        print(inorder(root))
        end=time.time()
        print("time taken for inorder binary tree is ",end-start)
    elif opt==2:
        start=time.time()
        print(preorder(root))
        end=time.time()
        print("time taken for preorder binary tree is",end-start)
    elif opt==3:
        start=time.time()
        print(postorder(root))
        end=time.time()
        print("time taken for post order binary tree is",end-start)
    elif opt==4:
       print("Exiting ...")
       break
    else:
        print("invaliad option")
        
    
             

