def binary_search(element, some_list):
    # 코드를 작성하세요.
    start = 0
    end = len(some_list)
    for i in range(start, end):
        mid_idx = (start + end) // 2
        if element > some_list[mid_idx]:
            start = mid_idx + 1
        elif element < some_list[mid_idx]:
            end = mid_idx - 1
        else:
            return mid_idx

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))