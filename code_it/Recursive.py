 # n의 각 자릿수의 합을 리턴
def sum_digits(n):
    # 코드를 작성하세요.
    if n < 10:
        return n
    else:
        
        str_n = str(n)
        return int(str_n[0]) + sum_digits(int(str_n[1:]))     
# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))
