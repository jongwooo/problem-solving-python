arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
m = len(arr)
n = len(arr[0])
new_arr = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        new_arr[i][j] = arr[j][n - i - 1]
for row in new_arr:
    print(*row)
