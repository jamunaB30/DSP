import time 
import numpy as np
import matplotlib.pyplot as plt
def insertion_sort(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and key<a[j]:
            a[j+1]=a[j]
            
            j-=1
        a[j+1]=key
    return a

a=[]
n=int(input("enter the element"))
for i in range(n):
    value=int(input("enter the element into a"))
    a.append(value)
print("array element before sorting are:",a)
print("array element after sorting are:",insertion_sort(a))

elements=np.array([i*500 for i in range(1,5)])
plt.xlabel('list length')
plt.ylabel('time complexity')
times=list()
for i in range(1,5):
    start=time.time()
    a=np.random.randint(500,size=i*500)
    insertion_sort(a)
    end=time.time()
    times.append(end-start)
    print("time taken for insertion sort in ",i*500,"element is",end-start,"s")
plt.plot(elements,times,label="insertion sort")
plt.grid()
plt.legend()
plt.show()
