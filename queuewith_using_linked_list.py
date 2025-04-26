class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertion(head):
    data = int(input("Enter the value to add node: "))
    ptr = Node(data)
    if head is None:
        head = ptr
    else:
        temp = head
        while temp.next is not None:  
            temp = temp.next
        temp.next = ptr  
    print(f"Inserted {data}")
    return head  

def deletion(head):
    if head is None:
        print("The queue is underflow")
    else:
        print(f"Successfully dequeued {head.data}")
        head = head.next  
    return head  

def traverse(head):
    if head is None:
        print("The queue is underflow")
    else:
        temp = head
        while temp is not None:
            print(temp.data, "-->", end=" ")
            temp = temp.next
        print("None")


head = None

while True:
    print("\nMenu")
    print("1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")
    
    opt = int(input("Enter the option: "))
    
    if opt == 1:
        head = insertion(head)  
    elif opt == 2:
        head = deletion(head)  
    elif opt == 3:
        traverse(head)
    elif opt == 4:
        print("Exit")
        break
    else:
        print("Invalid option")
