# 선택 정렬
def selection_sort(my_list):
    # 코드를 입력하세요.
    for i in range(0, len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i] > my_list[j]:
                my_list[j], my_list[i] = my_list[i], my_list[j]
    return my_list
     
some_list = [11, 3, 6, 4, 12, 1, 2]
selection_sort(some_list)
print(some_list)
