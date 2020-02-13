# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    # 코드를 작성하세요.
    value = str(n)
    if len(value) == 1:
        return int(n)
    else:
        return int(value[0]) + sum_digits(int(value[1:]))


print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))

