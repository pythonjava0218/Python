# 삽입 정렬
def insertion_sort(my_list):
    for i in range(len(my_list)):
        key = my_list[i]

        # i - 1부터 시작해서 왼쪽으로 하나씩 확인
        # 왼쪽 끝까지(0번 인덱스) 다 봤거나
        # key가 들어갈 자리를 찾으면 끝냄
        j = i - 1
        
        while j >= 0 and my_list[j] > key:
            my_list[j + 1] = my_list[j]
            j = j - 1

        # key가 들어갈 자리에 삽입
        # 왼쪽 끝까지 가서 j가 -1이면 0번 인덱스에 key를 삽입
        my_list[j + 1] = key

some_list = [11, 3, 6, 4, 12, 1, 2]
insertion_sort(some_list)
print(some_list)
 
