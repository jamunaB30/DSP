import time
import numpy as np
import matplotlib.pyplot as plt
def linearsearch(a, n, x):
   for i in range(0, n):
        if (a[i] == x):
            return(i)
   return(-1)
a = []
n = int(input("number of elements"))
for i in range(n):
    value = int(input("elements of the array"))
    a.append(value)
x = int(input("enter the element to search"))
result = linearsearch(a, n, x)
if (result == -1):
    print("Element not found")
else:
    print("Element found at index:", result)
    
elements = np.array([i * 500 for i in range(1, 5)])
plt.xlabel('list length')
plt.ylabel('time complexity ')
times = list()
for i in range(1, 5):
    start = time.time()
    a = np.random.randint(500, size=i * 500)
    n = i * 500
    linearsearch(a, n, x)
    end = time.time()
    times.append(end - start)
    print("time taken for linear search in ", i * 500, "elements is", end - start, "s")
plt.plot(elements, times, label="linearsearch")
plt.grid()
plt.legend()
plt.show()

