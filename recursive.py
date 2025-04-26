import time
def factorial(n):
    if n==1:
        return 1
    else:
        return(n*factorial(n-1))

def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return (fibonacci(n-1)+fibonacci(n-2))

def tower_of_honai(n,source,destination,auxiliaray):
    if n==1:
        print(f"Move disk from {souce} to {destination}")
        return
    tower_of_honai(n-1,source,auxiliary,destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_honai(n-1,auxiliary,destination,source)

while True:
    print("Menu")
    print("1.factorial")
    print("2.fibonacci")
    print("3.tower_of_honai")
    print("4.Exit")

    opt=int(input("Ënter the option"))
    if opt==1:
        n=int(input("Enter the number"))
        start=time.time()
        print(f"factorial of {n} is {factorial(n)}")
        end=time.time()
        print("time taken for factorial is",end-start,"s")
    elif opt==2:
        n=int(input("Enter the number"))
        start=time.time()
        print(f"fibonacci {n}s is {fibonacci(n)}")
        end=time.time()
        print("time taken for fibonacci is",end-start,"s")
    elif opt==3:
        n=int(input("Enter the number"))
        start=time.time()
        tower_of_honai(n,'A','B','C')
        end=time.time()
        print("time taken for tower of honai is",end-start,"s")
    elif opt==4:
        print("Exiting...")
        break
    else:
        print("Invalid option")
        
        
