from random import randint
numbers = []
user_numbers = []
i = 1
j = 0
strike = 0
ball = 0
count = 0

while len(numbers) < 3:
    new_number = randint(0, 9)

    while new_number in numbers:
        new_number = randint(0, 9)
    numbers.append(new_number)
print(numbers)
print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다. \n")


while strike != 3:
    print("세 수를 하나씩 차례대로 입력하세요")
    while len(user_numbers) < 3:
        num = int(input("%d번째 수를 입력하세요." % i))
        if num in user_numbers:
            print("중복되는 수 입니다.")
        elif num > 9:
            print("범위를 벗어난 수 입니다.")
        else:
            user_numbers.append(num)
            i += 1

            if numbers[j] == user_numbers[j]:
                strike += 1 
            elif user_numbers[j] in numbers:
                ball += 1
            j += 1
    print("%dS %dB \n" % (strike, ball))
    count += 1
    if strike != 3:        
        user_numbers = []
        i = 1
        j = 0
        strike = 0
        ball = 0
        
    else:
        print("축하합니다. %d번만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % count)
