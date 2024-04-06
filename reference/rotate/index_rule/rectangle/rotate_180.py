arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
m = len(arr)
n = len(arr[0])
new_arr = [[0] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        new_arr[i][j] = arr[m - i - 1][n - j - 1]
for row in new_arr:
    print(*row)
