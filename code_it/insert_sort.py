#some_list = [4, 5, 3, 1, 2]
def insertion_sort(my_list):
    # 코드를 입력하세요.
    for i in range(0, len(my_list)):

        key = my_list[i]

        j = i - 1

        while j >= 0 and my_list[j] > key:
            
            my_list[j + 1] = my_list[j]

            j = j - 1

        my_list[j + 1] = key
            
#some_list = [11, 3, 6, 4, 12, 1, 2]
some_list = [4, 5, 3, 1, 2]
insertion_sort(some_list)
print(some_list)
