def rotate_270(arr):
    return list(map(list, reversed(list(zip(*arr)))))


arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
new_arr = rotate_270(arr)
for row in new_arr:
    print(*row)
