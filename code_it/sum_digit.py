# 자리수 합 리턴
def sum_digit(num):
    str_num = str(num)
    result = 0
    for i in str_num: 
        result += int(i) 
    return result
        
# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
# 코드를 입력하세요.
 
sum_result = 0

for i in range(1, 1001):
    sum_result += sum_digit(i)
    
print(sum_result)
