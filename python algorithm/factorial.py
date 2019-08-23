def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)


print(fact(1))
print(fact(5))
print(fact(10))



'''
ex. n = 5


if 조건 성립 안되서 마지막 return 문장으로 내려감

5 * 4 


'''


