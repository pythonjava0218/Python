# 선택 정렬
my_list = [11, 3, 6, 4, 12, 1, 2]
 
# 코드를 입력하세요.
min_idx = my_list[0]

for i in range(0, len(my_list)):
    if min_idx > my_list[i]:
        min_idx = my_list[i]        
print(min_idx)
                   
