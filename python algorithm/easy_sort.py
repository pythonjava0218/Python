def find_min(a):
    n = len(a)
    min_idx = 0
    for i in range(n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx


def sel_sort(a):
    result = []
    while a:
        min_idx = find_min(a)
        value = a.pop(min_idx)
        result.append(value)
    return result

d = [4, 5, 6, 2, 3, 7]
print(find_min(d))

def find_min(a):
    n = len(a)
    min_idx = 0
