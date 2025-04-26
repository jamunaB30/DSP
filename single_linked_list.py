class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None  

    def insert_front(self, data):
        ptr = Node(data)
        ptr.next = self.head
        self.head = ptr
        print(f"\nInserted {data} at front\n")

    def insert_end(self, data):
        ptr = Node(data)
        if self.head is None:
            self.head = ptr 
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = ptr
        print(f"\nInserted {data} at end\n")

    def deletion_front(self):
        if self.head is None:
            print("\nList is empty")
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None  
            print(f"\nDeleted {temp.data} from beginning")

    def deletion_end(self):  
        if self.head is None:
            print("\nList is empty")
        elif self.head.next is None:  
            print(f"\nDeleted {self.head.data} from end")
            self.head = None
        else:
            temp = self.head
            prev = None
            while temp.next:
                prev = temp
                temp = temp.next
            prev.next = None
            print(f"\nDeleted {temp.data} from end")

    def display(self):
        if self.head is None:
            print("\nList is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next
            print("None")



ll = LinkedList()
while True:
    print("\nMenu")
    print("1. Insert at front")
    print("2. Insert at end")
    print("3. Deletion at beginning")
    print("4. Deletion at end")
    print("5. Display")
    print("6. Exit")
    
    opt = int(input("Enter your option: "))
    
    if opt == 1:
        val = int(input("Enter the value to insert at front: "))
        ll.insert_front(val)
    elif opt == 2:
        val = int(input("Enter the value to insert at end: "))
        ll.insert_end(val)
    elif opt == 3:
        ll.deletion_front()
    elif opt == 4:
        ll.deletion_end()
    elif opt == 5:
        ll.display()
    elif opt == 6:
        print("\nExiting...")
        break
    else:
        print("\nInvalid option! Please try again.")

