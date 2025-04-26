def simple_hash(key,size):
    return key % size
def string_hash(key,size):
    total=sum(ord(char)for char in key)
    return total % size
def multicative_hash(key,size):
    a=0.6180339887
    return int(size * ((key *a)%1))
def built_hash(key,size):
    return hash(key)%size
size=int(input("enter hash table size:"))
while True:
    opt=int(input("Enter the option"))
    if opt==1:
        key=int(input("Enter the integer value:"))
        print(f"Module hash{simple_hash(key,size)}")
    elif opt==2:
        key=input("Enter string value:")
        print(string_hash(key,size))
    elif opt==3:
        key=int(input("Enter the integer value:"))
        print(multicative_hash(key,size))
    elif opt==4:
        key=int(input("Enter the integer value:"))
        print(built_hash(key,size))
    elif opt==5:
        print("Exit")
        break
    else:
        print("inavliad option")
        
    
