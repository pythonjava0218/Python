# 화씨 온도에서 섭씨 온도로 바꿔주는 함수
def f_change_c(f):
    # 코드를 입력하세요.
    return (f  - 32) * 5 / 9

num = 0

# 테스트용 온도 리스트
temperature_list = [40, 15, 32, 64, -4, 11]

# 화씨 온도 출력
print("화씨 온도 리스트: " + str(temperature_list))

# 리스트의 값들을 화씨에서 섭씨로 변환

while num < len(temperature_list):
    temperature_list[num] = f_change_c(temperature_list[num])
    num += 1
# 섭씨 온도 출력
print("섭씨 온도 리스트: " + str(temperature_list))
