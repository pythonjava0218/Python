def consecutive_sum(start, end):
    # 코드를 작성하세요

    if start == end:
        return start

    return consecutive_sum(start, (start + end) // 2) + consecutive_sum((start + end) // 2 + 1, end)
# 테스트
print(consecutive_sum(1, 8))
# print(consecutive_sum(1, 100))
# print(consecutive_sum(1, 253))
# print(consecutive_sum(1, 388))


'''
Divide: 1부터 4까지의 합을 구하는 부분 문제와, 5부터 8까지의 합을 구하는 부분 문제로 나눈다.
Conquer: 1부터 4까지의 합을 구하고, 5부터 8까지의 합을 구한다.
Combine: 1부터 4까지의 합과 5부터 8까지의 합을 더한다.
'''