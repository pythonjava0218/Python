def fib_optimized(n):
    # 코드를 작성하세요.
    current = 1
    previous = 0
    temp = 0

    for i in range(1, n):

        '''
        temp = current
        current = previous + current
        previous = temp 
        '''
        current, previous = previous + current, current

    return current

# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))