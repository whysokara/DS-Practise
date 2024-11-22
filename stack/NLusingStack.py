def NearestGreatLeft(arr):
    ans = []
    stack = []

    for i in range(len(arr)):
        while len(stack) > 0 and stack[-1] < arr[i]:
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
            stack.append(arr[i])
        elif len(stack) > 0 and stack[-1] > arr[i]:
            ans.append(stack[-1])
            stack.append(arr[i])

    return ans


arr =  [6,2,5,3,1]
print(NearestGreatLeft(arr))


