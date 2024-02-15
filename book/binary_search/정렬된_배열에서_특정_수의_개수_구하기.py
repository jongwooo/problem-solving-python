from bisect import bisect_left, bisect_right


def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


n, x = map(int, input().split())
array = list(map(int, input().split()))
cnt = count_by_range(array, x, x)
print(-1 if cnt == 0 else cnt)
