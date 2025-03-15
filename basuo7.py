import matplotlib.pyplot as plt
import time
def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
arr = [int(x) for x in input("enter the arry elements separated by spaces:").split()]
x = int(input("enter the elements to search:"))
result=linear_search(arr,x)
if result == -1:
    print("Element is not present in array", result)
else:
    print("Element is present in array")
def measure_time_complexity(arr,x):
    start_time = time.time()
    linear_search(arr, x)
    end_time = time.time()
    return end_time - start_time
array_size = [10, 100, 1000, 10000, 1000000]
execution_times = []
for size in array_size:
    arr = [i for i in range(size)]
    x = size - 1
    time_taken = measure_time_complexity(arr,x)
    execution_times.append(time_taken)

total_time = sum(execution_times)
print(f"Total time complexity across all array sizes: {total_time:.4f} seconds")

plt.plot(array_size, execution_times)
plt.xlabel("Array size")
plt.ylabel("Execution time (seconds)")
plt.title("time complexity of linear search")
plt.show()