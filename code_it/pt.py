# 1 ~ 10 + 까지의 재귀함수 이용

'''
def func(n):
    if n == 1:
        return n
    return func(n - 1) + n


for i in range(1, 11):
    print(func(i))    
'''

# 피보나치 수열 => 첫 항과 두 번째 항목은 1로 시작

'''
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    return fib(n - 1) + fib(n - 2) 
 
for i in range(1, 11):
    print(fib(i))
'''

# 자릿수 합
'''
def sum_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)

def sum_digits(n):
    if n < 10:
        return n
    else:
        str_n = str(n)

        return sum_digits(int(str_n[0])) + sum_digits(int(str_n[1:]))
        
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))
'''

'''
#리스트 뒤집기 - 재귀함수 테스트

some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(some_list)
print(some_list[1:])
'''
'''
a = 1
b = 2 

if a < b:
    print("1")
print(a)
'''

'''
a = 4

while a <= 5:
    print(5)
    a = 5
    
'''
'''
my_list = [2, 1]

if len(my_list) < 3:
    if my_list[0] > my_list[1]:
        my_list[0], my_list[1] = my_list[1], my_list[0]
print(my_list)
'''
 

my_list = [4, 5, 3, 1, 2]

for i in range(len(my_list)):
    key = my_list[i]
    key = 5
    print(my_list)
