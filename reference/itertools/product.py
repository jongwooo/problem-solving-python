def product(n, new_arr):
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(len(arr)):
        product(n, new_arr + [arr[i]])


arr = [1, 2, 3, 4]
product(2, [])
