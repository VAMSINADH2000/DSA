
def find_pivot(arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + int((end - start)/2)
        print(mid)
        if (mid + 1 <= end):
            if (arr[mid] > arr[mid + 1]):
                return mid
        elif arr[mid - 1] > arr[mid]:
            return mid - 1
        if arr[start] >= arr[mid]:
            end  = mid - 1
        else:
            start = mid + 1
    return -1


arr = "40 44 52 62 72 80 81 87 90 97 104 113 119 127 134 144 145 154 164 167 171 172 179 4 14 15 19 24 29 34"
arr = [8,1]
print(find_pivot(arr))


