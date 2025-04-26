class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  

class DoublyLinkedList:
    def __init__(self):
        self.head = None  

    def insertion_front(self, data):
        ptr = Node(data)
        if self.head is None:
            
            self.head = ptr
        else:
            self.head.prev = ptr
            ptr.next = self.head
            self.head = ptr
        print(f"Inserted {data} at front")

    def insertion_end(self, data):
        ptr = Node(data)
        if self.head is None:
            self.head = ptr
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = ptr
            ptr.prev = temp
        print(f"Inserted {data} at end")

    def deletion_front(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            self.head = temp.next
            if self.head:
                self.head.prev = None  
            print(f"Deleted {temp.data} from front")

    def deletion_end(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next is None:  
            print(f"Deleted {self.head.data} from end")
            self.head = None
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.prev.next = None  
            print(f"Deleted {temp.data} from end")

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next
            print("None")


dll = DoublyLinkedList()
while True:
    print("\nMenu")
    print("1. Insert at front")
    print("2. Insert at end")
    print("3. Delete from front")
    print("4. Delete from end")
    print("5. Display")
    print("6. Exit")
    
    opt = int(input("Enter your option: "))
    
    if opt == 1:
        val = int(input("Enter the value to insert at front: "))
        dll.insertion_front(val)
    elif opt == 2:
        val = int(input("Enter the value to insert at end: "))
        dll.insertion_end(val)
    elif opt == 3:
        dll.deletion_front()
    elif opt == 4:
        dll.deletion_end()  
    elif opt == 5:
        dll.display()
    elif opt == 6:
        print("\nExiting...")
        break
    else:
        print("\nInvalid option! Please try again.")
