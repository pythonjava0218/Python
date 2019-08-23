# 빈 리스트 만들기
numbers = []

# numbers에 자연수 1부터 10까지 추가
 
i = 1

while i <= 10:
    numbers.append(i)
    i += 1
print(numbers)


# numbers에서 홀수 제거
 
i = 0


while i < len(numbers):
    if numbers[i] % 2 != 0:
        del numbers[i]
    else:
        i += 1
print(numbers)


# numbers의 인덱스 0 자리에 20이라는 값 삽입
# 코드를 입력하세요
numbers.insert(0, 20)
print(numbers)


# numbers를 정렬해서 출력
# 코드를 입력하세요

print(sorted(numbers))
