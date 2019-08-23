def sel_sort(a):
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]



d = [2, 5, 6, 3, 1, 7, 8, 4, 9]
sel_sort(d)
print(d)
