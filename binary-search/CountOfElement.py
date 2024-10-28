arr = [2,4,10,10,10,18,20]
target = 10

def firstOccurance(arr, target):
  l, r = 0, len(arr) - 1
  result = -1

  while l <= r:
    mid = (l+r)//2

    if arr[mid] == target:
      result = mid
      r = mid - 1
      
    elif arr[mid] < target:
      l = mid + 1
    else:
      r = mid - 1
  return result

def lastOccurance(arr, target):
  l, r = 0, len(arr) - 1
  result = -1

  while l <= r:
    mid = (l+r)//2

    if arr[mid] == target:
      result = mid
      l = mid + 1
      
    elif arr[mid] < target:
      l = mid + 1
    else:
      r = mid - 1
  return result

first = firstOccurance(arr,target)
last = lastOccurance(arr, target)
print(last-first+1)