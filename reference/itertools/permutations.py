def permutations(n, new_arr):
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            permutations(n, new_arr + [arr[i]])
            visited[i] = False


arr = [1, 2, 3, 4]
visited = [False] * len(arr)
permutations(2, [])
