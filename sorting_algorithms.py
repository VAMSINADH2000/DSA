def bubble_sort(arr):
    swap = False
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j + 1] = arr[j + 1],arr[j]
                swap = True
        if not swap:
            return arr
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        minindex = i
        for j in range(i+1,n):
            if arr[j] < arr[minindex]:
                minindex = j 
        arr[i], arr[minindex] = arr[minindex], arr[i]
    return arr

def insertion_sort(arr):
    for i  in range(len(arr)):
        j = i  
        while(arr[j - 1] > arr[j] and j > 0):
            arr[j - 1],arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr      
arr = [3,2,5,100,0,23] 
print(insertion_sort(arr))

