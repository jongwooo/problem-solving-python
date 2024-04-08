def gravity():
    global arr
    n = len(arr)
    m = len(arr[0])
    for i in range(n - 1):
        for j in range(m):
            p = i
            while 0 <= p and arr[p][j] == 1 and arr[p + 1][j] == 0:
                arr[p][j], arr[p + 1][j] = arr[p + 1][j], arr[p][j]
                p -= 1


arr = [[0, 1, 0], [1, 0, 1], [0, 1, 0], [0, 0, 1], [0, 1, 0]]
print('기존')
for a in arr:
    print(*a)
gravity()
print('변화')
for a in arr:
    print(*a)
