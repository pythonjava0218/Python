def trapping_rain(buildings):
    # 코드를 작성하세요
    rain = 0

    for i in range(1, len(buildings) - 1):
        left_tall = max(buildings[:i])
        right_tall = max(buildings[i:])

        short = min(left_tall, right_tall)

        '''
        zero_check = short - buildings[i]

        if zero_check < 0:
            rain += 0
        else:
            rain += zero_check
        '''
        rain += max(0, short - buildings[i])


    return rain

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
