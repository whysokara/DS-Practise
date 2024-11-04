arr = [1,4,3,5,4,3,2]
arr1 = [-1] * len(arr)


def finde(arr):
  for i in range(len(arr)-1):
    for j in range(i + 1, len(arr)):
      if arr[j] > arr[i]:
        arr1[i] = arr[j]
        break
  return arr1



finde(arr)