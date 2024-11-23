def NearestGreatRight(arr):
    stack = []
    ans = [None] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        ans[i] = -1 if not stack else stack[-1]
        stack.append(arr[i])

    return ans

def NearestSmallRight(arr):
    stack = []
    ans = [None] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        ans[i] = -1 if not stack else stack[-1]
        stack.append(arr[i])

    return ans

def NearestSmallLeft(arr):
    stack = []
    ans = [None] * len(arr)

    for i in range(len(arr)):
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        ans[i] = -1 if not stack else stack[-1]
        stack.append(arr[i])

    return ans

def NearestGreatLeft(arr):
    stack = []
    ans = [None] * len(arr)

    for i in range(len(arr)):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        ans[i] = -1 if not stack else stack[-1]
        stack.append(arr[i])

    return ans

