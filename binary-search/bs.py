def binary_search(arr, target):
    l,r = 0

    while l <= r:
        mid = l + (r-l) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            r = mid - 1
        else:
            l = mid + 1
    return -1

arr = [2,5,7,9,12,14,15,46,79]
target = 9
binary_search(arr, target)