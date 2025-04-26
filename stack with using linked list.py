class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insertion(head):
    data=int(input("enter the data"))
    new_node=Node(data)
    if(head==None):
        head=new_node
        print("inserted succesfully")
    else:
        temp=head
        head=new_node
        head.next=temp
        print("inseted succesfully")
    return head
def deletion(head):
    if(head==None):
        print("the stack is overflow")
    else:
        temp=head
        head=temp.next
        print("deleted succesfullty")
    return head
def traverse(head):
    if(head==None):
        print("the stack is poverflow")
    else:
        temp=head
        while temp!=None:
            print(temp.data,"-->",end="")
            temp=temp.next
head=None
while True:
    opt=int(input("enter the data"))
    if opt==1:
        head=insertion(head)
    elif opt==2:
        head=deletion(head)
    elif opt==3:
        traverse(head)
    elif opt==4:
        print("Exit")
        break
    else:
        print("invaliad option")


        
