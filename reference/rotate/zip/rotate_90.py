def rotate_90(arr):
    return list(map(list, zip(*arr[::-1])))


arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
new_arr = rotate_90(arr)
for row in new_arr:
    print(*row)
