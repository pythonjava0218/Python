# 두 요소의 위치를 바꿔주는 helper function
# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    # 코드를 작성하세요.
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
    return b
# 테스트 1
# list1 = [4, 3, 6, 2, 7, 1, 5]

# list1 = [1, 3, 5, 7, 9, 11, 13, 11]
# pivot_index1 = partition(list1, 0, len(list1) - 1)
# print(list1)
# print(pivot_index1)

# 테스트 2
# list2 = [6, 1, 2, 6, 3, 5, 4]
list2 = [1, 3, 2, 4, 6, 5, 6]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)
