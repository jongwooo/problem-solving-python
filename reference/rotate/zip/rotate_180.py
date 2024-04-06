def rotate_180(arr):
    return [a[::-1] for a in arr[::-1]]


arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
new_arr = rotate_180(arr)
for row in new_arr:
    print(*row)
