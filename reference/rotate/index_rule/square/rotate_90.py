arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(arr)
new_arr = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_arr[i][j] = arr[n - j - 1][i]
for row in new_arr:
    print(*row)
