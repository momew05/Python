import random as ran

array = []
for i in range(0, 16):
    array.append(ran.randint(0, 100))

def heapify(arr, n, i):
    root = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[i] < arr[l]:
        root = l

    if r < n and arr[root] < arr[r]:
        root = r

    if root != i:
        arr[i],arr[root] = arr[root],arr[i]

        heapify(arr, n, root)
    
n = len(array)

for i in range(n, -1, -1):
    heapify(array, n, i)

print(f"Входной массив:\n{array}\n")
print(f"Узлы бинарной кучи:")
for i in range(0, len(array)):
    if 2*i + 2 < len(array):
        print(" ")
        print(f"{array[i]}\n{array[2*i + 1]} {array[2*i + 2]}")

def heapsort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

print(f'\nОтсортированный массив: {heapsort(array)}')