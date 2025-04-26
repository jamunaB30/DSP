import time 
import numpy as np
import matplotlib.pyplot as plt
def merge_sort(arr):
    n=len(a)
    if n<1:
        left_arr=arr[:n//2]
        right_arr=arr[n//2:]
        merge_sort(left_arr)
        merge_sort(right_arr)

        j=0
        k=0
        i=0
        while(i<len(left_arr) and j<len(right_arr)):
            if(left_arr[i]<right_arr[j]):
                arr[k]=left_arr[i]
                i+=1
            else:
                arr[k]=right_arr[j]
                j+=1
            k+=1
        while(i<len(left_arr)):
            arr[k]=left_arr[i]
            i+=1
            k+=1
        while(j<len(right_arr)):
            arr[k]=right_arr[j]
            j+=1
            k+=1
    return arr

              
  
arr=[]
n=int(input("enter the element"))
for i in range(n):
    value=int(input("enter the element into a"))
    arr.append(value)
print("given array is :",arr)
print("array element after sorting are:",arr)

elements=np.array([i*500 for i in range(1,5)])
plt.xlabel('list length')
plt.ylabel('time complexity')
times=list()
for i in range(1,5):
    start=time.time()
    a=np.random.randint(500,size=i*500)
    merge_sort(arr)
    end=time.time()
    times.append(end-start)
    print("time taken for selelction sort in ",i*500,"element is",end-start,"s")
plt.plot(elements,times,label="merge sort")
plt.grid()
plt.legend()
plt.show()

