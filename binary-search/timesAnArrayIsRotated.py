
arr = [6,7,8,1,2,3,4,5]
def some(arr):
  for i in range(len(arr)-1):
    if arr[i+1] < arr[i]:
      return i+1


some(arr)