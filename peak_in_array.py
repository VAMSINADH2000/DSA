
def peak_in_array(array):
    start = 0
    end = len(array) - 1
    while(start<end):
        mid = start + int((end - start)/2)
        if array[mid] > arr[mid+1]:
            end = mid 
        elif array[mid] < arr[mid+1]:
            start = mid + 1
    return start


arr = [1,2,3,4,6,3,2,1]

print(peak_in_array(arr))