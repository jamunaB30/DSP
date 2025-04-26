import time 
import numpy as np
import matplotlib.pyplot as plt
def selection_sort(a):
    for i in range (len(a) - 1):
        small=i
        for j in range(i+1,len(a)):
            if a[j]<a[small]:
                small=j
        a[i],a[small]=a[small],a[i]
    return a


a=[]
n=int(input("enter the element"))
for i in range(n):
    value=int(input("enter the element into a"))ó
    a.append(value)
print("array element before sorting are:",a)
print("array element after dorting are:",selection_sort(a))

elements=np.array([i*500 for i in range(1,5)])
plt.xlabel('list length')
plt.ylabel('time complexity')
times=list()
for i in range(1,5):
    start=time.time()
    a=np.random.randint(500,size=i*500)
    selection_sort(a)
    end=time.time()
    times.append(end-start)
    print("time taken for selelction sort in ",i*500,"element is",end-start,"s")
plt.plot(elements,times,label="selection sort")
plt.grid()
plt.legend()
plt.show()

    
    
    
                
                
