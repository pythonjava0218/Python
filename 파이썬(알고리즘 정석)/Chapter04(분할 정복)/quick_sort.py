# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
# 이전 과제에서 작성한 코드를 붙여 넣으세요!
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 코드를 작성하세요.
    pivot = end
    b = start

    '''
    기준점 보다 큰 값 = 오른쪽
    기준점 보다 작은 값 = 왼쪽
    '''

    for i in range(start, end):
        if my_list[i] <= my_list[pivot]:
            swap_elements(my_list, i, b)
            b += 1

    swap_elements(my_list, b, pivot)
    pivot = b

    return pivot

# 퀵 정렬
def quicksort(my_list, start, end):
    # 코드를 작성하세요.
    if end - start < 1:
        return
    else:
        pivot = partition(my_list, start, end)
        quicksort(my_list, start, pivot - 1)
        quicksort(my_list, pivot + 1, end)

# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)


# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)


# # 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)