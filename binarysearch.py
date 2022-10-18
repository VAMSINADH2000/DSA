
def binary_search(array,search):
    start = 0
    end = len(array) - 1
    while(start<=end):
        mid = start + int((end - start)/2)
        if array[mid] > search:
            end = mid - 1
        elif array[mid] < search:
            start = mid + 1
        else:
            return mid
    return -1

array = [1,4,21,34,49,88,345]
binary_search(array,1)
binary_search(array,100)
binary_search(array,345)
binary_search(array,34)

