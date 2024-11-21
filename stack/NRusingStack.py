def nearestGreaterS(arr):
    stack = []
    ans = []

    for i in range(len(arr)-1,-1,-1):
        while len(stack) > 0 and stack[-1] < arr[i]:
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
            stack.append(arr[i])
        elif len(stack) > 0 and stack[-1] > arr[i]:
            ans.append(stack[-1])
            stack.append(arr[i])
    temp = ans[::-1]
    return temp


