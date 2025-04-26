import time
import numpy as np
import matplotlib.pyplot as plt
def binary_search(arr, low, high, x):
    if (high >= low):
        mid = (high + low) // 2
        if (arr[mid] == x):
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


arr = []
n = int(input("enter number of elements"))
for i in range(n):
    ele = int(input("enter elements of list:"))
    arr.append(ele)
print(arr)
x=int(input("enter the elements to search:"))
result=binary_search(arr,0,len(arr)-1,x)
if (result!= -1):
    print("elements is present")
else:
    print("elements is not present in array")


elements = np.array([i * 500 for i in range(1, 5)])
plt.xlabel('list length')
plt.ylabel('time complexity')
times=list()
for i in range(1, 5):
    start = time.time()
    arr = np.random.randint(500, size=i * 500)
    binary_search(arr, 0, len(arr)-1, x)
    end = time.time()
    times.append(end - start)
    print("time taken for binary search in", i * 500,"Elements is", end - start,"s")
plt.plot(elements, times, label="binary search")
plt.grid()
plt.legend()
plt.show()

