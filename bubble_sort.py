def create(n):
    for i in range(n):
        arr.append(int(input("Enter the element:")))
    print(arr)

def  bubble_sort(n):
    for i in range(n):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    print(arr)
    
arr=[]
n=int(input("Enter the number of element"))
print("Menu for bubble_sort")
print("1.create list")
print("2.sort the array using bubble sort")
print("3.Exit")
while True:
    opt=int(input("choose your option(1/2/3)"))
    if opt==1:
        create(n)
    elif opt==2:
        bubble_sort(n)
    elif opt==3:
        print("Exiting...")
        break;
    else:
        print("Invaliad option,please try again")
                
